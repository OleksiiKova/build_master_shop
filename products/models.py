import random
from django.db import models


class FirstLevelCategory(models.Model):
    """
    A category representing the first level in a hierarchy of product
    categories.
    Categories in this level are the broadest classification for products.

    Attributes:
        name (str): The name of the first-level category.
        friendly_name (str): A more user-friendly name for the category,
        optional.
    """
    class Meta:
        verbose_name_plural = 'First Level Categories'

    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """
        Returns the friendly name of the category.

        Returns:
            str: The friendly name of the category.
        """
        return self.friendly_name


class SecondLevelCategory(models.Model):
    """
    A category representing the second level in a hierarchy of product
    categories. This category is associated with the first-level category
    and represents a more specific classification.

    Attributes:
        name (str): The name of the second-level category.
        friendly_name (str): A more user-friendly name for the category,
        optional.
        first_level_category (ForeignKey): The related first-level category
        to which this belongs.
    """
    class Meta:
        verbose_name_plural = 'Second Level Categories'

    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    first_level_category = models.ForeignKey(
        FirstLevelCategory, on_delete=models.CASCADE,
        related_name='second_level_categories'
    )

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """
        Returns the friendly name of the second-level category.

        Returns:
            str: The friendly name of the second-level category.
        """
        return self.friendly_name


class ThirdLevelCategory(models.Model):
    """
    A category representing the third level in a hierarchy of product
    categories.
    This category is associated with a second-level category and represents
    the most
    specific classification.

    Attributes:
        name (str): The name of the third-level category.
        friendly_name (str): A more user-friendly name for the category,
        optional.
        second_level_category (ForeignKey): The related second-level category
        to which this belongs.
    """
    class Meta:
        verbose_name_plural = 'Third Level Categories'

    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    second_level_category = models.ForeignKey(
        SecondLevelCategory, on_delete=models.CASCADE,
        related_name='third_level_categories', blank=True, null=True
    )

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """
        Returns the friendly name of the third-level category.

        Returns:
            str: The friendly name of the third-level category.
        """
        return self.friendly_name


class Product(models.Model):
    """
    A product available for purchase, potentially associated with a category
    hierarchy (first-level, second-level, and third-level categories).
    This model includes attributes like price, stock, SKU, and image.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    first_level_category = models.ForeignKey(
        FirstLevelCategory, on_delete=models.SET_NULL,
        related_name='products', blank=True, null=True
    )
    second_level_category = models.ForeignKey(
        SecondLevelCategory, on_delete=models.SET_NULL,
        related_name='products', blank=True, null=True
    )
    third_level_category = models.ForeignKey(
        ThirdLevelCategory, on_delete=models.SET_NULL,
        related_name='products', blank=True, null=True
    )
    image = models.ImageField(null=True, blank=True)
    sku = models.CharField(max_length=64, null=True, blank=True, unique=True)
    rating = models.DecimalField(
        max_digits=2, decimal_places=1, default=None, null=True, blank=True)

    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    additional_attributes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_category_hierarchy(self):
        """
        Returns a list of categories associated with the product in
        hierarchical order.

        Returns:
            list: A list containing the categories (first, second, third
            level) associated with the product.
        """
        categories = []
        if self.first_level_category:
            categories.append(self.first_level_category)
        if self.second_level_category:
            categories.append(self.second_level_category)
        if self.third_level_category:
            categories.append(self.third_level_category)
        return categories

    def save(self, *args, **kwargs):
        """
        Override the save method to set the second-level and third-level
        categories based on the related category fields. Also generates a
        unique SKU if none exists.
        """
        if self.third_level_category:
            self.second_level_category = (
                self.third_level_category.second_level_category
            )
        if self.second_level_category:
            self.first_level_category = (
                self.second_level_category.first_level_category
            )

        if not self.sku:
            self.sku = self.generate_sku()
        super().save(*args, **kwargs)

    def generate_sku(self):
        """
        Generates a unique SKU for the product. The SKU starts with a prefix
        and is followed by a random 7-digit number. Ensures the SKU is unique
        in the database.

        Returns:
            str: A unique SKU for the product.
        """
        prefix = "bm-"
        while True:
            random_number = ''.join(random.choices('0123456789', k=7))
            new_sku = f"{prefix}{random_number}"
            if not Product.objects.filter(sku=new_sku).exists():
                return new_sku


class ProductVariant(models.Model):
    """
    Represents a specific variation of a product, such as size. Each
    variant has its own price, stock, and SKU.
    """
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='variants')
    size = models.CharField(max_length=64, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    sku = models.CharField(max_length=64, blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
        """
        Override the save method to generate a unique SKU for the variant based
        on the product's SKU and its size. If no SKU is provided, it is
        generated.
        """
        if not self.sku and self.product and self.product.sku:
            self.sku = self.generate_variant_sku()
        super().save(*args, **kwargs)

    def generate_variant_sku(self):
        """
        Generates a unique SKU for the product variant by combining the
        product's SKU with the variant's size. Ensures the SKU is unique.

        Returns:
            str: A unique SKU for the product variant.
        """
        base_sku = self.product.sku
        parts = [base_sku]

        if self.size:
            parts.append(self.size)

        new_sku = '-'.join(parts)

        return self.ensure_unique_sku(new_sku)

    def ensure_unique_sku(self, sku):
        """
        Ensures that the SKU is unique by checking if it already exists in the
        ProductVariant model. If it does, appends a counter to the SKU.

        Args:
            sku (str): The SKU to be checked.

        Returns:
            str: A unique SKU.
        """
        original_sku = sku
        counter = 1

        while ProductVariant.objects.filter(sku=sku).exists():
            sku = f"{original_sku}-{counter}"
            counter += 1

        return sku

    def __str__(self):
        return f"{self.product.name} - {self.size or ''}"
