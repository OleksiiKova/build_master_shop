import time
import json

from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404

import stripe

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product, ProductVariant
from profiles.models import UserProfile


class StripeWH_Handler:
    """Handle Stripe webhooks and process related events."""

    def __init__(self, request):
        """
        Initialize the handler with the request object.

        Args:
            request (HttpRequest): The HTTP request object containing the
            webhook data.
        """
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Send a confirmation email to the user after successful order placement.

        Args:
            order (Order): The order object containing order details.

        Sends an email to the customer's email address with a confirmation of
        the order.
        """
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def _clean_shipping_details(self, shipping_details):
        """
        Clean empty fields in the shipping details to prevent saving empty
        data.

        Args:
            shipping_details (ShippingDetails): The shipping details from the
            Stripe webhook.

        Returns:
            ShippingDetails: The cleaned shipping details with empty fields
            removed.
        """
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        return shipping_details

    def _update_user_profile(self, username, shipping_details, save_info):
        """
        Update the user profile with shipping details if 'save_info' is
        checked.

        Args:
            username (str): The username of the user making the order.
            shipping_details (ShippingDetails): The shipping details from the
            Stripe webhook.
            save_info (bool): Flag indicating whether the user wants to save
            their shipping info.

        Returns:
            UserProfile: The updated user profile if the user is authenticated,
            None otherwise.
        """
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_full_name = shipping_details.name
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_city = shipping_details.address.city
                profile.default_street_address1 = (
                    shipping_details.address.line1
                )
                profile.default_street_address2 = (
                    shipping_details.address.line2
                )
                profile.default_county = shipping_details.address.state
                profile.save()
            return profile
        return None

    def _get_existing_order(self, shipping_details, billing_details, cart, pid,
                            grand_total):
        """
        Attempt to retrieve an existing order from the database based on the
        given details.

        Args:
            shipping_details (ShippingDetails): The shipping details from the
            Stripe webhook.
            billing_details (BillingDetails): The billing details from the
            Stripe webhook.
            cart (str): A string representing the cart.
            pid (str): The Stripe payment ID.
            grand_total (float): The total amount charged for the order.

        Returns:
            tuple: A tuple containing a boolean indicating if an order exists,
            and the order object if found.
        """
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        return order_exists, order

    def _create_order(self, shipping_details, billing_details, cart, pid,
                      profile, grand_total):
        """
        Create a new order in the database if no existing order is found.

        Args:
            shipping_details (ShippingDetails): The shipping details from the
            Stripe webhook.
            billing_details (BillingDetails): The billing details from the
            Stripe webhook.
            cart (str): A string representing the cart.
            pid (str): The Stripe payment ID.
            profile (UserProfile): The user profile if the user is
            authenticated.
            grand_total (float): The total amount charged for the order.

        Returns:
            tuple: A tuple containing the created order and any error that
            occurred, or None if creation failed.
        """
        try:
            order = Order.objects.create(
                full_name=shipping_details.name,
                user_profile=profile,
                email=billing_details.email,
                phone_number=shipping_details.phone,
                country=shipping_details.address.country,
                postcode=shipping_details.address.postal_code,
                city=shipping_details.address.city,
                street_address1=shipping_details.address.line1,
                street_address2=shipping_details.address.line2,
                county=shipping_details.address.state,
                original_cart=cart,
                stripe_pid=pid,
            )
            # Add line items to the order
            for sku, item_data in json.loads(cart).items():
                variant = ProductVariant.objects.filter(sku=sku).first()
                if variant:
                    product = variant.product
                else:
                    product = get_object_or_404(Product, sku=sku)

                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    variant=variant,
                    quantity=item_data['quantity'],
                    sku=sku,
                )
                order_line_item.save()
            return order
        except Exception as e:
            return None, e

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event.

        Args:
            event (dict): The event data from the Stripe webhook.

        Returns:
            HttpResponse: A response indicating the event was handled.
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe, create
        an order or retrieve an existing one.

        Args:
            event (dict): The event data from the Stripe webhook.

        Returns:
            HttpResponse: A response indicating the success or failure
            of the webhook handling.
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)

        billing_details = stripe_charge.billing_details
        shipping_details = self._clean_shipping_details(intent.shipping)
        grand_total = round(stripe_charge.amount / 100, 2)

        # Update user profile if necessary
        profile = self._update_user_profile(
            intent.metadata.username, shipping_details, save_info)

        # Try to find an existing order
        order_exists, order = self._get_existing_order(
            shipping_details, billing_details, cart, pid, grand_total)

        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: '
                        f'Verified order already in database',
                status=200)
        else:
            order, error = self._create_order(
                shipping_details, billing_details, cart, pid, profile,
                grand_total
            )
            if not order:
                return HttpResponse(
                    content=f'Webhook received: {
                        event["type"]} | ERROR: {error}',
                    status=500)

            for line_item in order.lineitems.all():
                if line_item.variant:
                    line_item.variant.stock -= line_item.quantity
                    line_item.variant.save()
                else:
                    line_item.product.stock -= line_item.quantity
                    line_item.product.save()
                    
            self.request.session['cart'] = {}
            self.request.session.modified = True

        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: '
                    f'Created order in webhook',
            status=200)
