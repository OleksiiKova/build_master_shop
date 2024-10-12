from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, ProductVariant, FirstLevelCategory, SecondLevelCategory, ThirdLevelCategory

# Create your views here.
def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
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