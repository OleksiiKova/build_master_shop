from django.shortcuts import (
    render, redirect, reverse, HttpResponse
)
from django.contrib import messages
from products.models import Product, ProductVariant


def view_cart(request):
    """
    Render the shopping cart page.

    This view renders the template that displays the contents of the shopping
    cart.

    Attributes:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page for the shopping cart.
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, sku):
    """
    Add a product or variant to the shopping cart.

    This function retrieves a product or variant by SKU and adds it to the cart
    with the specified quantity and optional size. If the item already exists
    in the cart, it updates the quantity. Messages are shown to the user to
    confirm the addition or update of the item in the cart.

    Attributes:
        request (HttpRequest): The HTTP request object, which includes POST
        data for quantity, size, and the URL to redirect to after adding the
        item.
        sku (str): SKU of the product or variant to add to the cart.

    Returns:
        HttpResponseRedirect: Redirects to the specified URL or product list
        if the SKU is invalid.
    """
    product = Product.objects.filter(sku=sku).first()
    variant = None

    # If no product found by SKU, attempt to find a variant
    if not product:
        variant = ProductVariant.objects.filter(sku=sku).first()
        if variant:
            product = variant.product
        else:
            return redirect('product_list')

    quantity = int(request.POST.get('quantity', 1))
    selected_size = request.POST.get('size')
    redirect_url = request.POST.get('redirect_url', '/')

    stock = variant.stock if variant else product.stock
    if quantity > stock:
        messages.error(
            request,
            f'Only {stock} units of {product.name} (SKU: {sku}) are available in stock.',
        )
        return redirect(redirect_url)

    cart = request.session.get('cart', {})

    item_sku = variant.sku if variant else product.sku

    # Update quantity if item already in cart, else add new item
    if item_sku in cart:
        cart[item_sku]['quantity'] += quantity
        if selected_size:
            messages.add_message(
                request,
                26,
                f'Updated {product.name} quantity (Size: {selected_size}) '
                f'to {cart[sku]["quantity"]} item(s)',
                extra_tags='is_cart_related'
            )
        else:
            messages.add_message(
                request,
                26,
                f'Updated {product.name} quantity to {cart[sku]['quantity']} '
                f'item(s)',
                extra_tags='is_cart_related'
            )
    else:
        # Add new item with provided details
        cart[item_sku] = {
            'quantity': quantity,
            'product_name': product.name,
            'sku': item_sku,
            'size': selected_size,
            'price': str(variant.price if variant else product.price),
        }
        if selected_size:
            messages.add_message(
                request,
                26,
                f'Added {product.name} (Size: {selected_size}) to your cart',
                extra_tags='is_cart_related'
            )
        else:
            messages.add_message(
                request,
                26,
                f'Added {product.name} to your cart',
                extra_tags='is_cart_related'
            )

    request.session['cart'] = cart

    return redirect(redirect_url)


def adjust_cart(request, sku):
    """
    Adjust the quantity of a product in the shopping cart.

    This function updates the quantity of a product in the cart based on the
    SKU. If the quantity is set to zero, the product is removed from the cart.
    It provides feedback messages to the user for updates or removals.

    Attributes:
        request (HttpRequest): The HTTP request object, which contains POST
        data for quantity.
        sku (str): SKU of the product or variant to adjust in the cart.

    Returns:
        HttpResponseRedirect: Redirects to the cart view after adjusting the
        item quantity.
    """
    quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})
    product_name = cart[sku]['product_name']
    selected_size = cart[sku].get('size')

    product = Product.objects.filter(sku=sku).first()
    variant = None
    if not product:
        variant = ProductVariant.objects.filter(sku=sku).first()
        if variant:
            product = variant.product
    
    if not product:
        messages.error(request, f"Product with SKU {sku} not found.")
        return redirect(reverse('view_cart'))

    available_stock = variant.stock if variant else product.stock

    if quantity > available_stock:
        messages.error(
            request,
            f"Only {available_stock} item(s) of {product_name} are available in stock."
        )
        return redirect(reverse('view_cart'))

    if quantity > 0:
        # Update the quantity of the item in the cart
        cart[sku]['quantity'] = quantity
        if selected_size:
            messages.success(
                request,
                f'Updated {product_name} quantity (Size: {selected_size}) '
                f'to {cart[sku]['quantity']} item(s)'
            )
        else:
            messages.success(
                request,
                f'Updated {product_name} quantity to {cart[sku]['quantity']} '
                f'item(s)'
            )
    else:
        # Remove the item from the cart if quantity is zero
        cart.pop(sku)
        if selected_size:
            messages.success(
                request,
                f'Removed {product_name} (Size: {selected_size}) '
                f'from your cart'
            )
        else:
            messages.success(request, f'Removed {product_name} from your cart')

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


def remove_from_cart(request, sku):
    """
    Remove a product from the shopping cart.

    This function removes a product from the cart based on the SKU. If the
    product has a specified size, the size information is included in the
    removal message. If an error occurs during the removal, an error message
    is shown.

    Attributes:
        request (HttpRequest): The HTTP request object containing session data.
        sku (str): SKU of the product or variant to remove from the cart.

    Returns:
        HttpResponse: Returns a 200 status code on success or a 500 status
        code on failure.
    """
    cart = request.session.get('cart', {})
    product_name = cart[sku]['product_name']
    selected_size = cart[sku].get('size')

    try:
        cart = request.session.get('cart', {})
        cart.pop(sku)
        if selected_size:
            messages.success(
                request,
                f'Removed {product_name} (Size: {selected_size}) '
                f'from your cart',
                extra_tags='is_cart_related'
            )
        else:
            messages.success(
                request,
                f'Removed {product_name} from your cart',
                extra_tags='is_cart_related'
            )
        request.session['cart'] = cart

        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
