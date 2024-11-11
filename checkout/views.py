import json
import stripe

from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.conf import settings
from django.views.decorators.http import require_POST
from django.contrib import messages

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product, ProductVariant
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from cart.context_processors import cart_contents


@require_POST
def cache_checkout_data(request):
    """
    Cache the checkout data into Stripe's PaymentIntent metadata.

    This view is called when the checkout form is submitted. It processes
    the data, caches the user's cart information and other details into
    Stripe's PaymentIntent metadata, and then updates the PaymentIntent.

    The following data is sent to Stripe's metadata:
    - Cart: The current cart items (as a JSON string)
    - save_info: Whether the user chose to save their payment info for later
    - username: The username of the currently logged-in user

    If an error occurs during the request processing (e.g., a connection error
    with Stripe), an error message is sent to the user via the `messages`
    framework and a 400 HTTP response is returned with the error details.

    Args:
        request: The HTTP request object containing POST data.

    Returns:
        HttpResponse: A 200 HTTP response if successful, or a 400 HTTP
                      response with error message if something goes wrong.
    """
    try:
        # Extract the PaymentIntent ID from the client secret
        pid = request.POST.get('client_secret').split('_secret')[0]

        # Set the Stripe secret API key for authentication
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Modify the PaymentIntent's metadata with cart, save_info, and
        # username
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def get_cart(request):
    """
    Retrieves the current user's cart from the session.

    If the cart is empty, an error message is added and `None` is returned.
    Otherwise, the cart dictionary is returned.

    Args:
        request: The HTTP request object containing session data.

    Returns:
        dict: The cart data stored in the session or None if the cart is empty.
    """
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return None
    return cart


def create_order_from_form(request, cart):
    """
    Creates an order from the form data submitted by the user.

    The form data is collected from the POST request, validated, and then used
    to create a new order object. The cart is stored as JSON in the
    `original_cart`
    field of the order, and the Stripe PaymentIntent ID is saved.

    Args:
        request: The HTTP request object containing form data.
        cart: The current user's cart data.

    Returns:
        Order: The created order object if the form is valid, None if the
        form is invalid.
    """
    form_data = {
        'full_name': request.POST['full_name'],
        'email': request.POST['email'],
        'phone_number': request.POST['phone_number'],
        'country': request.POST['country'],
        'postcode': request.POST['postcode'],
        'city': request.POST['city'],
        'street_address1': request.POST['street_address1'],
        'street_address2': request.POST['street_address2'],
        'county': request.POST['county'],
    }
    order_form = OrderForm(form_data)
    if order_form.is_valid():
        order = order_form.save(commit=False)
        pid = request.POST.get('client_secret').split('_secret')[0]
        order.stripe_pid = pid
        order.original_cart = json.dumps(cart)
        order.save()
        return order
    else:
        messages.error(request, 'There was an error with your form. Please '
                       'double check your information.')
        return None


def create_order_line_items(order, cart):
    """
    Creates line items for the given order based on the products in the cart.

    For each product in the cart, an `OrderLineItem` is created and associated
    with the order. If a product is not found in the database, an error is
    shown and the order is deleted.

    Args:
        order: The order object to which line items will be added.
        cart: The current user's cart data.

    Returns:
        bool: True if line items were successfully created, False if an
        error occurred.
    """
    for sku, item_data in cart.items():
        try:
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
        except Product.DoesNotExist:
            messages.error(
                request,
                "One of the products in your cart wasn't "
                "found in our database. Please call us for assistance!"
            )
            order.delete()
            return False
    return True


def create_stripe_payment_intent(total):
    """
    Creates a Stripe PaymentIntent for the given order total.

    This PaymentIntent is used to process the payment through Stripe's API.
    The total is converted to the smallest currency unit (e.g., cents for USD).

    Args:
        total: The total amount for the order.

    Returns:
        stripe.PaymentIntent: A Stripe PaymentIntent object with the created
        intent.
    """
    stripe_total = round(total * 100)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    return stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )


def get_order_form(request):
    """
    Retrieves the order form, pre-filled with the user's profile information
    if authenticated.

    If the user is authenticated and has a profile, the form fields are
    populated with the saved default values from their profile. If the user
    does not have a profile or is not authenticated, a blank form is returned.

    Args:
        request: The HTTP request object containing user data.

    Returns:
        OrderForm: A populated or blank `OrderForm` instance.
    """
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            return OrderForm(initial={
                'full_name': profile.default_full_name,
                'email': profile.user.email,
                'phone_number': profile.default_phone_number,
                'country': profile.default_country,
                'postcode': profile.default_postcode,
                'city': profile.default_city,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'county': profile.default_county,
            })
        except UserProfile.DoesNotExist:
            return OrderForm()
    return OrderForm()


def checkout(request):
    """
    Handles the checkout process where the user fills out an order form,
    selects a payment method, and proceeds to payment.

    If the user submits the form, an order is created and line items are
    added based on the cart contents. Stripe payment intent is created, and
    the user is redirected to the checkout success page if everything goes
    well.

    Args:
        request: The HTTP request object containing form data and cart
        contents.

    Returns:
        HttpResponse: A rendered checkout page with the order form and
        payment intent details, or a redirect if an error occurs.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    if request.method == 'POST':
        cart = get_cart(request)
        if not cart:
            return redirect(reverse('products'))

        order = create_order_from_form(request, cart)
        if not order:
            return redirect(reverse('view_cart'))

        if create_order_line_items(order, cart):
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number]))

    else:
        cart = get_cart(request)
        if not cart:
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        intent = create_stripe_payment_intent(total)

        order_form = get_order_form(request)

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you '
                         'forget to set it in your environment?')

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """
    Handle successful checkout and save order details to the user's profile
    if authenticated.

    This view is triggered when an order has been successfully processed.
    It attaches the user's profile to the order if the user is authenticated
    and saves the order details (such as address and contact information) to
    the user's profile if they opt to save their information for future use.
    A success message is then shown
    to the user, and the cart session is cleared.

    Args:
        request (HttpRequest): The HTTP request object containing the session
        and user data.
        order_number (str): The unique order number associated with the
        successful order.

    Returns:
        HttpResponse: A rendered template that shows the order details and a
        success message.
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    for item in order.lineitems.all():
        product = item.product
        variant = item.variant

        if variant:
            variant.stock -= item.quantity
            variant.save()
        else:
            product.stock -= item.quantity
            product.save()

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # If the user wants to save their information, update their profile
        if save_info:
            profile_data = {
                'default_full_name': order.full_name,
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_city': order.city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            # Update the profile with the new details from the order
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    # Clear the cart from the session after a successful order
    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
