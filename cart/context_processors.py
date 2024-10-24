from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product, ProductVariant
# from .models import Cart

def cart_contents(request):

    cart_items = []
    total_cost = 0
    product_count = 0

    STANDARD_DELIVERY_COST = Decimal(7.00)
    EXPRESS_DELIVERY_COST = Decimal(20.00)
    free_delivery_threshold = Decimal(50.00)
    free_delivery_delta = 0
    cart = request.session.get('cart', {})

    for sku, item_data in cart.items():
        variant = ProductVariant.objects.filter(sku=sku).first()
        if variant:
            product = variant.product
        else:
            product = get_object_or_404(Product, sku=sku)

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

    
    selected_delivery_method = request.session.get('selected_delivery_method', 'standard')
    if not cart_items:
        delivery_cost = 0
    else:
        delivery_cost = (
            STANDARD_DELIVERY_COST if selected_delivery_method == 'standard' else EXPRESS_DELIVERY_COST
        )

    
    # if cart_items:
    #     total_cost = sum(item.product.price * item.quantity for item in cart.items.all())

    if total_cost >= free_delivery_threshold and selected_delivery_method == 'standard':
        delivery_cost = 0
    else:
        free_delivery_delta = free_delivery_threshold - total_cost if selected_delivery_method == 'standard' else 0

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

