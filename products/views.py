from django.shortcuts import render
from .models import Product, ProductVariant, FirstLevelCategory, SecondLevelCategory, ThirdLevelCategory

# Create your views here.
def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)