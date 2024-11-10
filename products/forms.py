from django import forms
from django.forms import inlineformset_factory
from .models import (
    Product, ProductVariant, FirstLevelCategory, SecondLevelCategory,
    ThirdLevelCategory
)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'first_level_category',
                  'second_level_category', 'third_level_category', 'price',
                  'stock', 'additional_attributes', 'image',]


class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = ['size', 'price', 'stock', 'additional_attributes']


ProductVariantFormSet = inlineformset_factory(
    Product, ProductVariant,
    form=ProductVariantForm,
    extra=1,
    can_delete=True
)
