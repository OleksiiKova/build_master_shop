from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the BlogPost model.

    This class customizes the Django admin interface for the BlogPost model.
    It pre-populates the 'slug' field from the 'title' field, displays relevant
    fields in the list view, and enables searching and filtering.

    Attributes:
        prepopulated_fields (dict): Specifies that the 'slug' field should be
        automatically populated based on the 'title'.
        list_display (tuple): Fields to display in the list view, including the
        title, published date, and view count.
    """
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'published_date', 'views')


admin.site.register(BlogPost, BlogPostAdmin)
