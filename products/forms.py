from django import forms
from django.forms import inlineformset_factory
from .models import (
    Product, ProductVariant, FirstLevelCategory, SecondLevelCategory,
    ThirdLevelCategory
)


class ProductForm(forms.ModelForm):
    """
    Form for creating and updating Product instances.

    This form allows you to enter data related to a product such as its name,
    description, price, stock, category relationships (first, second, and
    third-level), additional attributes, and an image.
    """
    class Meta:
        model = Product
        fields = ['name', 'description', 'first_level_category',
                  'second_level_category', 'third_level_category', 'price',
                  'stock', 'additional_attributes', 'image']


class ProductVariantForm(forms.ModelForm):
    """
    Form for creating and updating ProductVariant instances.

    This form allows you to input information about product variants, such as
    the size, price, stock quantity, and additional attributes. Each variant
    represents a specific variation of a product (e.g., different sizes or
    colors).
    """
    class Meta:
        model = ProductVariant
        fields = ['size', 'price', 'stock', 'additional_attributes']


ProductVariantFormSet = inlineformset_factory(
    Product, ProductVariant,
    form=ProductVariantForm,
    extra=1,
    can_delete=True
)
