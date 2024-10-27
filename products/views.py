from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, ProductVariant, FirstLevelCategory, SecondLevelCategory, ThirdLevelCategory
from .forms import ProductForm, ProductVariantForm, ProductVariantFormSet
from django.forms import modelformset_factory

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


def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        variant_formset = ProductVariantFormSet(request.POST, prefix='variants')

        if product_form.is_valid() and variant_formset.is_valid():
            product = product_form.save()
            
            # Save each variant associated with this product
            variants = variant_formset.save(commit=False)
            for variant in variant_formset.save(commit=False):
                variant.product = product  # Link variant to the saved product
                variant.save()

            # Delete any variants marked for deletion in the formset
            for form in variant_formset.deleted_forms:
                form.instance.delete()

            # Optional: call save_m2m() if there are any Many-to-Many relations
            variant_formset.save_m2m()

            messages.success(request, 'Successfully added product!')
            return redirect('product_detail_by_sku', sku=product.sku)
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')

    else:
        product_form = ProductForm()
        variant_formset = ProductVariantFormSet(prefix='variants')
    
    template = 'products/add_product.html'
    context = {
        'product_form': product_form,
        'variant_formset': variant_formset,
    }
    
    return render(request, template, context)


def edit_product(request, sku):
    # Fetch the product instance by SKU
    product = get_object_or_404(Product, sku=sku)

    if request.method == 'POST':
        # Prepopulate the forms with data from the request and the existing product instance
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        variant_formset = ProductVariantFormSet(request.POST, request.FILES, prefix='variants', instance=product)

        if product_form.is_valid() and variant_formset.is_valid():
            # Save the product and the associated variants
            product = product_form.save()
            variants = variant_formset.save(commit=False)

            for variant in variants:
                variant.product = product  # Link variant to the product
                variant.save()

            # Handle any variants marked for deletion
            for form in variant_formset.deleted_forms:
                form.instance.delete()

            # Optional: call save_m2m() if there are Many-to-Many relationships
            variant_formset.save_m2m()

            messages.success(request, 'Successfully updated product!')
            return redirect('product_detail_by_sku', sku=product.sku)
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')

    else:
        # If the request is not POST, initialize the forms with existing product data
        product_form = ProductForm(instance=product)
        variant_formset = ProductVariantFormSet(prefix='variants', instance=product)
    
    template = 'products/edit_product.html'
    context = {
        'product_form': product_form,
        'variant_formset': variant_formset,
        'product': product,
    }
    
    return render(request, template, context)


def delete_product(request, sku):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
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