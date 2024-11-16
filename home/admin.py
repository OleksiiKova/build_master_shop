from django.contrib import admin
from .models import ContactMessage


# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    Admin view for managing ContactMessage model.

    This admin interface allows viewing and managing ContactMessage instances.
    It displays the 'message' and 'read' fields in the admin list view.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
    """
    list_display = ('name', 'message', 'read',)
