from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product, ProductVariant

# Create your views here.

def view_cart(request):
    """
    A view that renders the cart contents page
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, sku):
    
    product = Product.objects.filter(sku=sku).first()
    variant = None
    
    if not product:
        
        variant = ProductVariant.objects.filter(sku=sku).first()
        if variant:
            product = variant.product
        else:
            return redirect('product_list')

    quantity = int(request.POST.get('quantity', 1))
    selected_size = request.POST.get('size')
    redirect_url = request.POST.get('redirect_url', '/')

    cart = request.session.get('cart', {})

    item_sku = variant.sku if variant else product.sku

    if item_sku in cart:
        cart[item_sku]['quantity'] += quantity
    else:
        cart[item_sku] = {
            'quantity': quantity,
            'product_name': product.name,
            'sku': item_sku,
            'size': selected_size,
            'price': str(variant.price if variant else product.price),
        }
        messages.success(request, f'Added {product.name} to your bag')

    request.session['cart'] = cart

    return redirect(redirect_url)


def adjust_cart(request, sku):
    
    quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[sku]['quantity'] = quantity
    else:
        cart.pop(sku)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, sku):
    
    try:
        cart = request.session.get('cart', {})
        cart.pop(sku)
        request.session['cart'] = cart

        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
