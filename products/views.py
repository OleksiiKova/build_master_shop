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
    category_hierarchy = []
    sort = None
    direction = None

    if request.GET:
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

        first_level = request.GET.get('first_level')
        second_level = request.GET.get('second_level')
        third_level = request.GET.get('third_level')

        if first_level:
            products = products.filter(first_level_category__name=first_level)
            first_level_category = FirstLevelCategory.objects.get(name=first_level)
            category_hierarchy.append({
                'name': first_level_category.name,
                'friendly_name': first_level_category.friendly_name
            })

        if second_level:
            products = products.filter(second_level_category__name=second_level)
            second_level_category = SecondLevelCategory.objects.get(name=second_level)
            category_hierarchy.append({
                'name': second_level_category.name,
                'friendly_name': second_level_category.friendly_name
            })

        if third_level:
            products = products.filter(third_level_category__name=third_level)
            third_level_category = ThirdLevelCategory.objects.get(name=third_level)
            category_hierarchy.append({
                'name': third_level_category.name,
                'friendly_name': third_level_category.friendly_name
            })

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

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


# def product_detail(request, product_id, variant_sku=None):
#     """ A view to show individual product details """

#     product = get_object_or_404(Product, pk=product_id)

#     if variant_sku is None and product.variants.exists():
#         first_variant = product.variants.first()
#         return redirect('product_detail_variant', product_id=product.id, variant_sku=first_variant.sku)

#     selected_variant = None
#     if variant_sku:
#         selected_variant = get_object_or_404(ProductVariant, sku=variant_sku, product=product)

#     context = {
#         'product': product,
#         'selected_variant': selected_variant
#     }

#     return render(request, 'products/product_detail.html', context)


def product_detail_by_sku(request, sku):
    variant = ProductVariant.objects.filter(sku=sku).first()

    if variant:
        product = variant.product
        selected_variant = variant
        current_sku = variant.sku
    else:
        product = get_object_or_404(Product, sku=sku)
        
        first_variant = product.variants.first()
        if first_variant:
            return redirect('product_detail_by_sku', sku=first_variant.sku)
        
        selected_variant = None
        current_sku = product.sku

    context = {
        'product': product,
        'selected_variant': selected_variant,
        'current_sku': current_sku,
    }

    return render(request, 'products/product_detail.html', context)