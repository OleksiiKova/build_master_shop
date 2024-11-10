from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django_countries.fields import CountryField

from products.models import Product


class UserProfile(models.Model):
    """
    A model representing a user's profile that stores default shipping
    information and order history.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_full_name = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True
    )
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True
    )
    default_postcode = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler to create or update a user profile when a User instance
    is saved.

    Args:
        sender (Model): The model class that sent the signal (User).
        instance (User): The actual instance of the User model.
        created (bool): A boolean indicating whether the instance was created.
        **kwargs: Additional arguments passed by the signal.

    If the user is newly created, a corresponding UserProfile is also created.
    If the user already exists, the existing profile is saved (no changes are
    made to it).
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()


class Review(models.Model):
    """
    A model representing a review for a product.

    Methods:
        __str__(): Returns a string representation of the review including
        user, product, and rating.
        update_product_rating(): Recalculates and updates the average rating
        for the associated product.
    """
    RATING_CHOICES = [
        (1, '1 - Low'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_updated = models.BooleanField(default=False)

    class Meta:
        unique_together = ('product', 'user')

    def __str__(self):
        return f"{self.user} - {self.product} - {self.rating}"

    def update_product_rating(self):
        """
        Recalculates and updates the average rating of the associated product.
        This method is called whenever a review is saved or deleted to maintain
        the accuracy of the product's rating.

        Args:
            None

        Updates:
            The average rating of the product is calculated and saved to the
            product instance.
        """
        avg_rating = self.product.reviews.aggregate(
            Avg('rating'))['rating__avg']
        self.product.rating = avg_rating
        self.product.save()


@receiver(post_save, sender=Review)
def update_product_rating_on_save(sender, instance, **kwargs):
    """
    Signal handler that updates the product rating when a review is saved.

    Args:
        sender (Model): The model class that sent the signal (Review).
        instance (Review): The actual instance of the Review model.
        **kwargs: Additional arguments passed by the signal.

    This function triggers the `update_product_rating` method whenever a new
    review is saved,
    ensuring that the product's rating is up to date.
    """
    instance.update_product_rating()


@receiver(post_delete, sender=Review)
def update_product_rating_on_delete(sender, instance, **kwargs):
    """
    Signal handler that updates the product rating when a review is deleted.

    Args:
        sender (Model): The model class that sent the signal (Review).
        instance (Review): The actual instance of the Review model.
        **kwargs: Additional arguments passed by the signal.

    This function triggers the `update_product_rating` method whenever a
    review is deleted,
    ensuring that the product's rating is updated accordingly.
    """
    instance.update_product_rating()


class Wishlist(models.Model):
    """
    A model representing a user's wishlist for products they are interested in.

    Methods:
        __str__(): Returns a string representation of the wishlist entry.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username}'s wishlist - {self.product.name}"
