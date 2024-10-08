from django.contrib import admin
from .models import FirstLevelCategory, SecondLevelCategory, ThirdLevelCategory, Product, ProductVariant

admin.site.register(FirstLevelCategory)
admin.site.register(SecondLevelCategory)
admin.site.register(ThirdLevelCategory)
admin.site.register(Product)
admin.site.register(ProductVariant)
