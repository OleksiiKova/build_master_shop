from django.contrib import admin
from .models import (
    FirstLevelCategory, SecondLevelCategory, ThirdLevelCategory, Product,
    ProductVariant
)


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1
    readonly_fields = ('sku',)


class ProductAdmin(admin.ModelAdmin):
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
    list_display = (
        'product',
        'size',
        'price',
    )

    ordering = ('product',)
    readonly_fields = ('sku',)


class FirstLevelCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
    )

    ordering = ('friendly_name',)


class SecondLevelCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'first_level_category',
    )

    ordering = ('first_level_category',)


class ThirdLevelCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'second_level_category',
    )

    ordering = ('second_level_category',)


admin.site.register(FirstLevelCategory, FirstLevelCategoryAdmin)
admin.site.register(SecondLevelCategory, SecondLevelCategoryAdmin)
admin.site.register(ThirdLevelCategory, ThirdLevelCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)
