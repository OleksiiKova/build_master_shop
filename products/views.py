from django.db.models import Q
from django.db.models.functions import Lower
from django.forms import modelformset_factory

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import (
    Product, ProductVariant, FirstLevelCategory, SecondLevelCategory,
    ThirdLevelCategory
)
from checkout.models import OrderLineItem
from profiles.forms import ReviewForm
from .forms import ProductForm, ProductVariantForm, ProductVariantFormSet


def get_sorted_products(request, products):
    """
    Sorts the products based on the request parameters.

    Args:
        request (HttpRequest): The request object containing the `sort` and
        `direction` parameters.
        products (QuerySet): The queryset of products to be sorted.

    Returns:
        tuple: A tuple containing:
            - products (QuerySet): The sorted products.
            - sort (str or None): The sort field (e.g., 'name', 'category').
            - direction (str or None): The sort direction ('asc' or 'desc').

    Sorts products by name (case-insensitive) or category, and allows
    ascending/descending order.
    """
    sort = None
    direction = None
    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        if sortkey == 'name':
            sortkey = 'lower_name'
            products = products.annotate(lower_name=Lower('name'))
        if sortkey == 'category':
            sortkey = 'first_level_category__name'
        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        products = products.order_by(sortkey)

    return products, sort, direction


def filter_by_category(request, products):
    """
    Filters products based on category levels (first, second, third).

    Args:
        request (HttpRequest): The request object containing the `first_level`,
        `second_level`, and `third_level` category filters.
        products (QuerySet): The queryset of products to be filtered.

    Returns:
        tuple: A tuple containing:
            - products (QuerySet): The filtered products.
            - category_hierarchy (list): A list of dictionaries with category
            names and friendly names.
            - first_level (str or None): The first level category filter value.
            - second_level (str or None): The second level category filter
            value.
            - third_level (str or None): The third level category filter value.

    Filters products by the selected category levels (if provided) and
    constructs the category hierarchy with friendly names.
    """
    category_hierarchy = []
    first_level = request.GET.get('first_level')
    second_level = request.GET.get('second_level')
    third_level = request.GET.get('third_level')

    if first_level:
        products = products.filter(first_level_category__name=first_level)
        first_level_category = FirstLevelCategory.objects.get(
            name=first_level)
        category_hierarchy.append({
            'name': first_level_category.name,
            'friendly_name': first_level_category.friendly_name
        })

    if second_level:
        products = products.filter(second_level_category__name=second_level)
        second_level_category = SecondLevelCategory.objects.get(
            name=second_level)
        category_hierarchy.append({
            'name': second_level_category.name,
            'friendly_name': second_level_category.friendly_name
        })

    if third_level:
        products = products.filter(third_level_category__name=third_level)
        third_level_category = ThirdLevelCategory.objects.get(
            name=third_level)
        category_hierarchy.append({
            'name': third_level_category.name,
            'friendly_name': third_level_category.friendly_name
        })

    return products, category_hierarchy, first_level, second_level, third_level


def search_products(request, products):
    """
    Searches for products based on the query string in the request.

    Args:
        request (HttpRequest): The request object containing the search query.
        products (QuerySet): The queryset of products to search through.

    Returns:
        tuple: A tuple containing:
            - products (QuerySet): The filtered products matching the search
            query.
            - query (str or None): The search query entered by the user.

    If a search query is provided, filters products by name and description.
    If the query is empty, displays an error message.
    """
    query = None
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return products, None

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    return products, query


def product_list(request):
    """
    A view to display all products with sorting, filtering by category,
    and search functionality.

    Args:
        request (HttpRequest): The request object containing any search
                               or filtering parameters.

    Returns:
        HttpResponse: The rendered HTML page displaying the filtered and
                      sorted products.

    The function handles:
        - Sorting products based on request parameters
        (e.g. by name or category).
        - Filtering products by category (first, second, third levels).
        - Searching products by name or description based on a query string.
    """
    products = Product.objects.all()

    for product in products:
        # Проверяем наличие товара на складе
        if product.stock == 0:
            product.out_of_stock = True
        else:
            product.out_of_stock = False

    category_hierarchy = []

    # Get sorted products
    products, sort, direction = get_sorted_products(request, products)

    # Filter products by category
    (products, category_hierarchy, first_level, second_level,
     third_level) = filter_by_category(
        request, products)

    # Search products by query
    products, query = search_products(request, products)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'first_level': first_level,
        'second_level': second_level,
        'third_level': third_level,
        'category_hierarchy': category_hierarchy,
        'current_sorting': current_sorting
    }

    return render(request, 'products/products.html', context)


def get_product_and_variant_by_sku(sku):
    """
    Fetch the product and its variant by SKU.

    Args:
        sku (str): The SKU (Stock Keeping Unit) of the product or variant.

    Returns:
        tuple: A tuple containing:
            - Product: The product object associated with the SKU.
            - ProductVariant or None: The variant of the product (if any).
            - SKU (str): The SKU of the product or variant.

    The function first attempts to retrieve a product variant by SKU.
    If a variant is found, it returns the product, variant, and SKU.
    If no variant is found, it retrieves the product by SKU and returns
    the product along with its first variant (if available).
    """
    variant = ProductVariant.objects.filter(sku=sku).first()
    if variant:
        return variant.product, variant, variant.sku
    else:
        product = get_object_or_404(Product, sku=sku)
        first_variant = product.variants.first()
        if first_variant:
            return product, first_variant, first_variant.sku
        return product, None, product.sku


def check_user_verified(request, product):
    """
    Check if the user has purchased the product.

    Args:
        request (HttpRequest): The request object, containing the user's
        session.
        product (Product): The product object to check against the user's
        purchase history.

    Returns:
        bool: True if the user has purchased the product, otherwise False.

    This function checks if the user is authenticated, and if so, verifies
    whether they have purchased the given product by checking the order
    history of the user associated with the current request.
    """
    if request.user.is_authenticated:
        return OrderLineItem.objects.filter(
            order__user_profile=request.user.userprofile,
            product=product
        ).exists()
    return False


def handle_review_submission(request, product):
    """
    Handle the review form submission.

    Args:
        request (HttpRequest): The request object, containing user data and
        form data.
        product (Product): The product object that the review is for.

    Returns:
        HttpResponse: A redirect to the current page, either with a success or
        error message.
        ReviewForm: If the method is not POST, an empty review form is
        returned.

    This function processes the review submission for a product. It checks if
    the user is authenticated and if the form is valid. If the user has already
    reviewed the product, an error message is shown. Otherwise, the review is
    saved and a success message is displayed. In case of errors, an appropriate
    message is shown.
    """
    if request.method == "POST" and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            existing_review = product.reviews.filter(user=request.user).first()
            if existing_review:
                messages.error(
                    request,
                    'You have already submitted a review for this product.')
            else:
                try:
                    review = form.save(commit=False)
                    review.product = product
                    review.user = request.user
                    review.save()
                    messages.success(request, 'Successfully added review!')
                except IntegrityError:
                    messages.error(
                        request,
                        'There was an error submitting your review.')
            return redirect(request.path)
    return ReviewForm()  # Return an empty form if not POST


def product_detail_by_sku(request, sku):
    """
    Display the product details by SKU.

    Args:
        request (HttpRequest): The request object, containing user data and
        any form submissions.
        sku (str): The SKU of the product to display.

    Returns:
        HttpResponse: A rendered HTML page showing the product details,
        including reviews, review form, and product information.

    This function retrieves the product and its variant based on the SKU. It
    also checks if the user has previously purchased the product and whether
    they have submitted a review. If the user is authenticated, it processes
    review submissions. The page is populated with product details, reviews,
    and related information, and the appropriate context is passed to the
    template for rendering.
    """
    # Get product and variant based on SKU
    product, selected_variant, current_sku = (
        get_product_and_variant_by_sku(sku)
    )
    # Check if the user is verified (has purchased this product)
    is_verified_user = check_user_verified(request, product)

    # Get product reviews and check if the user has already reviewed
    reviews = product.reviews.all().order_by('-created_at')
    user_review = reviews.filter(
        user=request.user).first() if request.user.is_authenticated else None
    user_has_reviewed = user_review is not None

    # Handle review submission
    form_review = handle_review_submission(request, product)

    # Check stock availability
    if selected_variant:
        is_out_of_stock = selected_variant.stock == 0
    else:
        is_out_of_stock = product.stock == 0

    context = {
        'product': product,
        'reviews': reviews,
        'form_review': form_review,
        'user_has_reviewed': user_has_reviewed,
        'user_review': user_review,
        'is_verified_user': is_verified_user,
        'selected_variant': selected_variant,
        'current_sku': current_sku,
        'is_out_of_stock': is_out_of_stock,
    }

    return render(request, 'products/product_detail.html', context)


def check_superuser_permission(request):
    """
    Check if the user has superuser privileges.

    Args:
        request (HttpRequest): The HTTP request object, containing user data.

    Returns:
        HttpResponse or None: Redirects to the home page with an error message
        if the user is not a superuser, otherwise returns None.

    This function checks whether the authenticated user is a superuser
    (store owner). If the user is not a superuser,
    they are shown an error message and redirected to the home page. If the
    user is a superuser, the function does nothing and returns `None` to allow
    further processing.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    return None


def save_product_and_variants(product_form, variant_formset):
    """
    Save the product and its variants, handling any deletions of variants.

    Args:
        product_form (forms.ModelForm): The form instance for the product to
        be saved.
        variant_formset (forms.BaseModelFormSet): The formset instance for the
        product's variants.

    Returns:
        product (Product): The saved product instance.

    This function saves a product and its associated variants. It handles
    the following:
    - Saving the product data.
    - Saving each variant associated with the product, linking each variant
      to the correct product.
    - Deleting any variants that are marked for deletion in the formset.
    - Saving any many-to-many relationships (if applicable).

    The function returns the saved `Product` instance.
    """
    product = product_form.save()

    # Save each variant associated with the product
    variants = variant_formset.save(commit=False)
    for variant in variants:
        variant.product = product  # Link variant to the product
        variant.save()

    # Delete any variants marked for deletion
    for form in variant_formset.deleted_forms:
        form.instance.delete()

    # Save many-to-many relationships (if any)
    variant_formset.save_m2m()

    return product


@login_required
def add_product(request):
    """
    Add a new product to the store.

    Args:
        request (HttpRequest): The request object, containing form data and
        user session.

    Returns:
        HttpResponse: A redirect to the product detail page if the product is
        added successfully, or a rendered form page with error messages if the
        form is invalid.

    This view allows the store owner (superuser) to add a new product to the
    store.
    It handles both product details and associated variants. The function
    performs the following:
    - Checks if the user is a superuser and denies access if not.
    - Validates and processes the product and variant forms on a POST request.
    - Saves the product and variants if the forms are valid.
    - Displays success or error messages based on the result.
    - Renders the form on a GET request to display the empty form for a new
    product.
    """
    permission_check = check_superuser_permission(request)
    if permission_check:
        return permission_check  # Early exit if not a superuser

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        variant_formset = ProductVariantFormSet(
            request.POST, prefix='variants')

        if product_form.is_valid() and variant_formset.is_valid():
            product = save_product_and_variants(product_form, variant_formset)
            messages.success(request, 'Successfully added product!')
            return redirect('product_detail_by_sku', sku=product.sku)
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')

    else:
        product_form = ProductForm()
        variant_formset = ProductVariantFormSet(prefix='variants')

    context = {
        'product_form': product_form,
        'variant_formset': variant_formset,
    }

    return render(request, 'products/add_product.html', context)


@login_required
def edit_product(request, sku):
    """
    Edit an existing product.

    Args:
        request (HttpRequest): The request object, containing form data and
        user session.
        sku (str): The SKU of the product to be edited.

    Returns:
        HttpResponse: A redirect to the product detail page if the product
        is updated successfully, or a rendered form page with error messages
        if the form is invalid.

    This view allows the store owner (superuser) to edit an existing product
    in the store.
    The function performs the following:
    - Checks if the user is a superuser and denies access if not.
    - Fetches the product based on the SKU and allows modifications.
    - Validates and processes the product and variant forms on a POST request.
    - Saves the updated product and its variants if the forms are valid.
    - Displays success or error messages based on the result.
    - Renders the form on a GET request to display the existing product data
    for editing.
    """
    permission_check = check_superuser_permission(request)
    if permission_check:
        return permission_check  # Early exit if not a superuser

    product = get_object_or_404(Product, sku=sku)

    if request.method == 'POST':
        product_form = ProductForm(request.POST,
                                   request.FILES, instance=product)
        variant_formset = ProductVariantFormSet(
            request.POST, request.FILES, prefix='variants', instance=product)

        if product_form.is_valid() and variant_formset.is_valid():
            product = save_product_and_variants(product_form, variant_formset)
            messages.success(request, 'Successfully updated product!')
            return redirect('product_detail_by_sku', sku=product.sku)
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')

    else:
        product_form = ProductForm(instance=product)
        variant_formset = ProductVariantFormSet(
            prefix='variants', instance=product)

    context = {
        'product_form': product_form,
        'variant_formset': variant_formset,
        'product': product,
    }

    return render(request, 'products/edit_product.html', context)


@login_required
def delete_product(request, sku):
    """
    Delete a product from the store.

    Args:
        request (HttpRequest): The request object, containing user data
        and form submissions.
        sku (str): The SKU of the product to be deleted.

    Returns:
        HttpResponse: A redirect to the product listing page after deletion,
        or a rendered confirmation page if the request method is GET.

    This view allows the store owner (superuser) to delete an existing product
    from the store.
    The function performs the following:
    - Checks if the user is a superuser and denies access if not.
    - Fetches the product based on the SKU.
    - Deletes the product upon a POST request and displays a success message.
    - Displays a confirmation page on a GET request for the user to confirm
    deletion.
    """
    permission_check = check_superuser_permission(request)
    if permission_check:
        return permission_check  # Early exit if not a superuser

    product = get_object_or_404(Product, sku=sku)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted!')
        return redirect(reverse('products'))

    template = 'products/delete_product.html'
    context = {
        'product': product,
    }
    return render(request, template, context)
