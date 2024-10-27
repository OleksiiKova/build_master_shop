from django.db import models
import random


class FirstLevelCategory(models.Model):

    class Meta:
        verbose_name_plural = 'First Level Categories'

    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length = 254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class SecondLevelCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Second Level Categories'

    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length = 254, null=True, blank=True)
    first_level_category = models.ForeignKey(FirstLevelCategory, on_delete=models.CASCADE, related_name='second_level_categories')

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class ThirdLevelCategory(models.Model):
    
    class Meta:
        verbose_name_plural = 'Third Level Categories'

    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length = 254, null=True, blank=True)
    second_level_category = models.ForeignKey(SecondLevelCategory, on_delete=models.CASCADE, related_name='third_level_categories', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    first_level_category = models.ForeignKey(FirstLevelCategory, on_delete=models.SET_NULL, related_name='products', blank=True, null=True)
    second_level_category = models.ForeignKey(SecondLevelCategory, on_delete=models.SET_NULL, related_name='products', blank=True, null=True)
    third_level_category = models.ForeignKey(ThirdLevelCategory, on_delete=models.SET_NULL, related_name='products', blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    sku = models.CharField(max_length=64, null=True, blank=True, unique=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=None, null=True, blank=True)
    
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    additional_attributes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_category_hierarchy(self):
        categories = []
        if self.first_level_category:
            categories.append(self.first_level_category)
        if self.second_level_category:
            categories.append(self.second_level_category)
        if self.third_level_category:
            categories.append(self.third_level_category)
        return categories

    def save(self, *args, **kwargs):
        if self.third_level_category:
            self.second_level_category = self.third_level_category.second_level_category
        if self.second_level_category:
            self.first_level_category = self.second_level_category.first_level_category

        if not self.sku:
            self.sku = self.generate_sku()
        super().save(*args, **kwargs)
    
    def generate_sku(self):
        prefix = "bm-"
        while True:
            random_number = ''.join(random.choices('0123456789', k=7))
            new_sku = f"{prefix}{random_number}"
            if not Product.objects.filter(sku=new_sku).exists():
                return new_sku


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    size = models.CharField(max_length=64, blank=True, null=True)
    additional_attributes = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    sku = models.CharField(max_length=64, blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.sku and self.product and self.product.sku:
            self.sku = self.generate_variant_sku()
        super().save(*args, **kwargs)

    def generate_variant_sku(self):
        base_sku = self.product.sku
        parts = [base_sku]

        if self.size:
            parts.append(self.size)

        new_sku = '-'.join(parts)

        return self.ensure_unique_sku(new_sku)

    def ensure_unique_sku(self, sku):
        original_sku = sku
        counter = 1

        while ProductVariant.objects.filter(sku=sku).exists():
            sku = f"{original_sku}-{counter}"
            counter += 1

        return sku

    def __str__(self):
        return f"{self.product.name} - {self.size or ''}"