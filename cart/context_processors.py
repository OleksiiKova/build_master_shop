from decimal import Decimal
from django.contrib import messages
from products.models import Product, ProductVariant


def cart_contents(request):
    """
    Retrieve and calculate details of the shopping cart contents.

    This function computes the total cost, delivery cost, and other cart
    details.
    It manages cart items in session storage, verifies if each product or
    variant exists,
    and removes non-existing items with a warning message.

    Attributes:
        request (HttpRequest): The HTTP request object, which contains
        session data.

    Returns:
        dict: A dictionary with the cart details, including:
            - cart_items (list): List of items in the cart with details on
            product, variant, quantity, etc.
            - total_cost (Decimal): Total cost of all products in the cart.
            - delivery_cost (Decimal): Cost of delivery based on selected
            delivery method and cart total.
            - free_delivery_threshold (Decimal): The minimum total cost
            required for free delivery.
            - free_delivery_delta (Decimal): Amount left to reach the free
            delivery threshold.
            - grand_total (Decimal): Final total including delivery cost.
            - selected_delivery_method (str): The selected delivery method
            ('standard' or 'express').
            - product_count (int): Total count of individual products in the
            cart.
    """
    cart_items = []
    total_cost = 0
    product_count = 0

    STANDARD_DELIVERY_COST = Decimal(7.00)
    EXPRESS_DELIVERY_COST = Decimal(20.00)
    free_delivery_threshold = Decimal(50.00)
    free_delivery_delta = 0
    cart = request.session.get('cart', {})

    items_to_delete = []

    for sku, item_data in cart.items():
        variant = ProductVariant.objects.filter(sku=sku).first()
        if variant:
            product = variant.product
            price = variant.price
        else:
            product = Product.objects.filter(sku=sku).first()
            if product:
                price = product.price
            else:
                items_to_delete.append(sku)
                continue

        quantity = item_data['quantity']
        total_cost += quantity * (variant.price if variant else product.price)
        product_count += quantity
        cart_items.append({
            'sku': sku,
            'quantity': quantity,
            'product': product,
            'variant_sku': item_data.get('variant_sku'),
            'size': item_data.get('size'),
        })

    for sku in items_to_delete:
        del cart[sku]
        messages.warning(
            request,
            f'The product {sku} has been removed from the cart '
            'because it no longer exists.'
        )
    request.session['cart'] = cart

    selected_delivery_method = request.session.get(
        'selected_delivery_method',
        'standard'
    )
    if not cart_items:
        delivery_cost = 0
    else:
        delivery_cost = (
            STANDARD_DELIVERY_COST
            if selected_delivery_method == 'standard'
            else EXPRESS_DELIVERY_COST
        )

    if (total_cost >= free_delivery_threshold and
            selected_delivery_method == 'standard'):
        delivery_cost = 0
    else:
        free_delivery_delta = (
            free_delivery_threshold - total_cost
            if selected_delivery_method == 'standard'
            else 0
        )
    grand_total = total_cost + delivery_cost

    return {
        'cart_items': cart_items,
        'total_cost': total_cost,
        'delivery_cost': delivery_cost,
        'free_delivery_threshold': free_delivery_threshold,
        'free_delivery_delta': free_delivery_delta,
        'grand_total': grand_total,
        'selected_delivery_method': selected_delivery_method,
        'product_count': product_count,
    }
