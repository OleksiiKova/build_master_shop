from decimal import Decimal
# from .models import Cart

def cart_contents(request):

    cart_items = []
    total_cost = 0
    product_count = 0

    STANDARD_DELIVERY_COST = Decimal(7.00)
    EXPRESS_DELIVERY_COST = Decimal(20.00)
    free_delivery_threshold = Decimal(50.00)
    free_delivery_delta = 0

    # if request.user.is_authenticated:
    #     try:
    #         cart_items = Cart.objects.get(user=request.user)
    #     except Cart.DoesNotExist:
    #         cart_items = None
    # else:
    #     cart_items = None

    selected_delivery_method = request.session.get('selected_delivery_method', 'standard')
    delivery_cost = STANDARD_DELIVERY_COST if selected_delivery_method == 'standard' else EXPRESS_DELIVERY_COST
    
    if cart_items:
        total_cost = sum(item.product.price * item.quantity for item in cart.items.all())

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
    }

