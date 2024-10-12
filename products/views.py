from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, ProductVariant, FirstLevelCategory, SecondLevelCategory, ThirdLevelCategory

# Create your views here.
def product_list(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    first_level = None
    second_level = None
    third_level = None

    if request.GET:
        first_level = request.GET.get('first_level')
        second_level = request.GET.get('second_level')
        third_level = request.GET.get('third_level')

        if first_level:
            products = products.filter(first_level_category__name=first_level)

        if second_level:
            products = products.filter(second_level_category__name=second_level)

        if third_level:
            products = products.filter(third_level_category__name=third_level)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'first_level': first_level,
        'second_level': second_level,
        'third_level': third_level,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id, variant_sku=None):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    if variant_sku is None and product.variants.exists():
        first_variant = product.variants.first()
        return redirect('product_detail_variant', product_id=product.id, variant_sku=first_variant.sku)

    selected_variant = None
    if variant_sku:
        selected_variant = get_object_or_404(ProductVariant, sku=variant_sku, product=product)

    context = {
        'product': product,
        'selected_variant': selected_variant
    }

    return render(request, 'products/product_detail.html', context)