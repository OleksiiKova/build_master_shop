from django import forms
from .widgets import CustomClearableFileInput
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
                  'stock', 'additional_attributes', 'image']

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)


class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = ['size', 'price', 'stock', 'additional_attributes']


ProductVariantFormSet = inlineformset_factory(
    Product, ProductVariant,  # Parent model, Child model
    form=ProductVariantForm,
    extra=1,  # Number of empty forms displayed initially
    can_delete=True  # Allow deleting variants
)
