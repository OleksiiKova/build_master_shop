from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'comment', 'created_at')
    search_fields = ['product', 'user']
    list_filter = ('product', 'user',)

admin.site.register(Review, ReviewAdmin)
