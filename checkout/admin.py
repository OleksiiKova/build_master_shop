from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'order_date', 'delivery_method',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_cart', 'stripe_pid',)

    fields = ('user_profile', 'order_number', 'order_date', 'full_name',
              'email', 'phone_number', 'street_address1', 'street_address2',
              'city', 'county', 'country', 'postcode', 'delivery_method',
              'delivery_cost', 'order_total', 'grand_total')

    list_display = ('full_name', 'order_number', 'order_date',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-order_date',)


admin.site.register(Order, OrderAdmin)
