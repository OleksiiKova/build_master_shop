import uuid
import random
import string

from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField

from products.models import Product, ProductVariant
from profiles.models import UserProfile


class Order(models.Model):
    """
    Order model to handle customer orders, storing details like customer info,
    delivery method, and total costs.
    """
    DELIVERY_CHOICES = [
        ('standard', 'Standard Delivery'),
        ('express', 'Express Delivery'),
    ]

    order_number = models.CharField(max_length=16, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_method = models.CharField(
        max_length=10,
        choices=DELIVERY_CHOICES,
        default='standard')
    delivery_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0)
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0)
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number starting with 'ORD-'
        and 10 characters long. The order number must be unique in the
        database.

        Returns:
            str: The generated unique order number.
        """
        prefix = "ORD-"
        while True:  # Loop until a unique order number is generated
            # Generate 8 random alphanumeric characters
            unique_part = ''.join(
                random.choices(string.ascii_uppercase + string.digits, k=8))
            order_number = prefix + unique_part

            # Check if the order number already exists in the database
            if not Order.objects.filter(order_number=order_number).exists():
                break

        return order_number

    def update_total(self):
        """
        Update the order's total, delivery cost, and grand total whenever
        a line item is added. The method calculates the total cost of the items
        in the order, adds the appropriate delivery cost based on the order's
        total, and calculates the grand total.

        This method must be called whenever the line items change or the
        delivery method is updated.
        """
        # Calculate order total
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0

        # Calculate delivery cost based on the chosen method

        if self.order_total > 0:
            if self.order_total < 50:  # Orders below 50 EUR
                self.delivery_cost = 7  # Fixed 7 EUR for standard delivery
            else:
                self.delivery_cost = 0  # Free delivery for orders over 50 EUR
        else:
            self.delivery_cost = 0

        # Calculate grand total (order total + delivery cost)
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to ensure the order number is set
        before the order is saved in the database.

        If the order number has not been set, generate a new unique order
        number before saving the order.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return the order number as the string representation of the Order
        object.
        """
        return self.order_number


class OrderLineItem(models.Model):
    """
    A line item represents an individual product or product variant within
    an order.
    It links the product (or variant) to an order, records the quantity,
    and calculates the total price for that item in the order.
    """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, null=True, blank=True,
                                on_delete=models.SET_NULL)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    sku = models.CharField(max_length=64, null=True, blank=True,
                           editable=False)
    lineitem_total = models.DecimalField(max_digits=10, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the SKU and lineitem total price before saving the object.
        If the line item is based on a variant, the variant's price is used;
        otherwise, the product's price is used.
        """
        # Set the SKU: if a variant is present, use its SKU; otherwise, use
        # the product's SKU.
        if self.variant:
            self.sku = self.variant.sku
        else:
            self.sku = self.product.sku

        # Calculate the line item total: quantity * price of the
        # product/variant.
        if self.variant:
            self.lineitem_total = self.variant.price * self.quantity
        else:
            self.lineitem_total = self.product.price * self.quantity

        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return a human-readable string representation of the line item.
        The string will include the SKU and whether it is a variant or just
        a product and the order number it belongs to.
        """
        if self.variant:
            return f'SKU {self.variant.sku} (variant) on order '
            f'{self.order.order_number}'
        else:
            return f'SKU {self.product.sku} on order {self.order.order_number}'
