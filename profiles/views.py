from math import modf

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import UserProfile, Review, Wishlist
from .forms import UserProfileForm, ReviewForm

from products.models import (
    Product, ProductVariant
)
from checkout.models import Order


@login_required
def profile(request):
    """
    Display the user's profile.

    This function retrieves the user's profile and displays the profile form,
    allowing the user to update their information.
    If the form is submitted with valid data, the profile is updated.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile updated successfully')
        else:
            messages.error(
                request,
                'Update failed. Please ensure the form is valid.'
            )
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history_list(request):
    """
    Display the user's order history (list of all orders).
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all().order_by('-order_date')

    template = 'profiles/order_history_list.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    Display the order history for a specific order.

    Args:
        request (HttpRequest): The request object containing user data and
        any form submissions.
        order_number (str): The order number for the order to display.

    Returns:
        HttpResponse: A rendered HTML page displaying the details of a past
        order.

    This function retrieves a specific order based on the order number. It
    then sends an informational message to the user indicating that this is a
    past order, and renders a page with the order details. The page also
    includes a flag indicating that the user has come from their profile page,
    if applicable. The order is passed to the template for rendering.
    """
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_order_history_list': True,
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """
    Edit an existing review written by the user for a product.

    Args:
        request (HttpRequest): The request object containing user data and
        form submissions.
        review_id (int): The ID of the review to be edited.

    Returns:
        HttpResponse: A rendered HTML page displaying the review edit form
        or redirects to another page.

    This function retrieves a specific review for the logged-in user by its
    ID, allowing the user to edit their review.
    If the form is valid, the review is updated, marked as updated, and saved.
    Afterward, the user is either redirected
    to the product detail page or their list of reviews, depending on the
    value of the 'next' parameter.
    """
    review = get_object_or_404(Review, id=review_id, user=request.user)
    form = ReviewForm(request.POST or None, instance=review)

    next_page = request.GET.get('next', 'product_detail_by_sku')

    if form.is_valid():
        review = form.save(commit=False)
        review.is_updated = True
        review.save()
        messages.success(request, 'Your review was updated successfully!')
        if next_page == 'my_reviews':
            return redirect('user_reviews')
        return redirect('product_detail_by_sku', sku=review.product.sku)

    context = {'form': form, 'review': review, 'next': next_page}
    return render(request, 'profiles/edit_review.html', context)


@login_required
def delete_review(request, review_id):
    """
    Delete a review written by the user for a product.

    Args:
        request (HttpRequest): The request object containing user data and
        form submissions.
        review_id (int): The ID of the review to be deleted.

    Returns:
        HttpResponse: A redirect to either the user's review list or the
        product detail page.

    This function retrieves a specific review for the logged-in user by its
    ID and deletes it upon confirmation (via a POST request).
    After deletion, the user is either redirected to their list of reviews or
    back to the product's detail page, depending on the 'next' parameter.
    """
    review = get_object_or_404(Review, id=review_id, user=request.user)
    next_page = request.GET.get('next', 'product_detail_by_sku')
    if request.method == "POST":
        product_sku = review.product.sku
        review.delete()
        messages.success(request, 'Your review was deleted successfully!')
        if next_page == 'my_reviews':
            return redirect('user_reviews')
        return redirect('product_detail_by_sku', sku=product_sku)

    context = {'review': review, 'next': next_page}
    return render(request, 'profiles/delete_review.html', context)


@login_required
def user_reviews(request):
    """
    Display a list of reviews written by the logged-in user.

    Args:
        request (HttpRequest): The request object containing user data.

    Returns:
        HttpResponse: The rendered 'user_reviews' template displaying the
        user's reviews.

    This function retrieves all reviews written by the logged-in user,
    ordered by creation date in descending order.
    It then renders the 'profiles/user_reviews.html' template, passing the
    list of reviews as context.
    """
    reviews = Review.objects.filter(
        user=request.user).select_related('product').order_by('-created_at')

    context = {
        'reviews': reviews
    }
    return render(request, 'profiles/user_reviews.html', context)


@login_required
def add_to_wishlist(request):
    """
    Add a product to the user's wishlist.

    This view handles adding a product to the authenticated user's wishlist.
    It determines the product based on the SKU extracted from the redirect URL.
    If the product is already in the wishlist, a message is shown to inform the
    user.
    """
    redirect_url = request.POST.get('redirect_url', '')
    if not redirect_url:
        messages.error(request, 'Invalid URL.')
        return redirect('products')

    path_parts = redirect_url.strip('/').split('/')
    sku_from_url = path_parts[-1]

    variant = ProductVariant.objects.filter(sku=sku_from_url).first()
    if variant:
        product = variant.product
    else:
        product = get_object_or_404(Product, sku=sku_from_url)

    if not Wishlist.objects.filter(
            user=request.user, product=product).exists():
        Wishlist.objects.create(user=request.user, product=product)
        messages.success(request, 'Successfully added to your wishlist!')
    else:
        messages.info(request, 'This product is already in your wishlist.')

    return redirect(redirect_url)


@login_required
def wishlist(request):
    """
    Display the user's wishlist.

    This view retrieves all the items in the authenticated user's wishlist and
    renders them in a template. The user must be logged in to access this view.

    Args:
        request (HttpRequest): The request object containing user data.

    Returns:
        HttpResponse: Renders the 'profiles/wishlist.html' template with the
        user's wishlist items.

    This function retrieves all wishlist items for the logged-in user and
    passes them to the template
    for rendering. The template displays the user's wishlist, including product
    details for each item.
    """
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request,
                  'profiles/wishlist.html', {'wishlist_items': wishlist_items})


@login_required
def remove_from_wishlist(request, item_id):
    """
    Remove an item from the user's wishlist.

    This view allows the authenticated user to remove a product from their
    wishlist.
    The item is identified by its ID, and the user must be logged in to access
    this functionality.
    """
    wishlist_item = get_object_or_404(Wishlist, id=item_id, user=request.user)

    wishlist_item.delete()
    messages.success(request, 'Successfully deleted from your wishlist!')

    return redirect('wishlist')
