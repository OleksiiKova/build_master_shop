from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    Admin interface for managing product reviews.

    This class customizes the display and functionality of the Review model
    in the Django admin interface.
    """
    list_display = ('product', 'user', 'rating', 'comment', 'created_at')
    search_fields = ['product', 'user']
    list_filter = ('product', 'user',)


admin.site.register(Review, ReviewAdmin)
