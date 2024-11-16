from django.contrib import admin
from .models import (
    FirstLevelCategory, SecondLevelCategory, ThirdLevelCategory, Product,
    ProductVariant
)


class ProductVariantInline(admin.TabularInline):
    """
    Inline model for ProductVariant, which allows managing variants
    directly from the Product's admin page.

    Attributes:
        model: The model to be included in the inline (ProductVariant).
        extra: Number of empty forms to display for adding new ProductVariants.
        readonly_fields: Fields to be displayed as read-only in the admin
        interface.
    """
    model = ProductVariant
    extra = 1
    readonly_fields = ('sku',)


class ProductAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Product model.

    Attributes:
        list_display: Fields to display in the list view of Products.
        ordering: Default ordering of products based on the first level
        category.
        inlines: Include the ProductVariantInline to allow managing
        ProductVariants.
        readonly_fields: Fields to be displayed as read-only in the admin
        interface.
    """
    list_display = (
        'name',
        'first_level_category',
        'second_level_category',
        'third_level_category',
        'price',
        'rating',
        'image',
    )

    ordering = ('first_level_category',)

    inlines = [ProductVariantInline]
    readonly_fields = ('sku',)


class ProductVariantAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the ProductVariant model.

    Attributes:
        list_display: Fields to display in the list view of ProductVariants.
        ordering: Default ordering of ProductVariants based on the Product.
        readonly_fields: Fields to be displayed as read-only in the admin
        interface.
    """
    list_display = (
        'product',
        'size',
        'price',
    )

    ordering = ('product',)
    readonly_fields = ('sku',)


class FirstLevelCategoryAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the FirstLevelCategory model.

    Attributes:
        list_display: Fields to display in the list view of
        FirstLevelCategory.
        ordering: Default ordering by friendly name of the category.
    """
    list_display = (
        'friendly_name',
    )

    ordering = ('friendly_name',)


class SecondLevelCategoryAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the SecondLevelCategory model.

    Attributes:
        list_display: Fields to display in the list view of
        SecondLevelCategory.
        ordering: Default ordering by the first level category.
    """
    list_display = (
        'friendly_name',
        'first_level_category',
    )

    ordering = ('first_level_category',)


class ThirdLevelCategoryAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the ThirdLevelCategory model.

    Attributes:
        list_display: Fields to display in the list view of ThirdLevelCategory.
        ordering: Default ordering by the second level category.
    """
    list_display = (
        'friendly_name',
        'second_level_category',
    )

    ordering = ('second_level_category',)


# Register the models with the admin site
admin.site.register(FirstLevelCategory, FirstLevelCategoryAdmin)
admin.site.register(SecondLevelCategory, SecondLevelCategoryAdmin)
admin.site.register(ThirdLevelCategory, ThirdLevelCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)
