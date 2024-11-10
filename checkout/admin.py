from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Inline admin interface for OrderLineItem within the OrderAdmin.

    This class allows you to display and edit `OrderLineItem` instances
    directly within the `Order` model form in the Django admin interface.

    Attributes:
        model (OrderLineItem): The model to be displayed inline in the
        `OrderAdmin`.
        readonly_fields (tuple): Fields to display as read-only, in this case,
        the line item total.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Order model.

    This class customizes the Django admin interface for the Order model,
    displaying relevant fields, allowing inlines for OrderLineItems, and
    specifying various administrative options.

    Attributes:
        inlines (tuple): Inline admin configurations, in this case,
        OrderLineItemAdminInline.
        readonly_fields (tuple): Fields to be displayed as read-only.
        fields (tuple): Fields to be displayed on the Order admin form.
        list_display (tuple): Fields to display in the list view.
        ordering (tuple): Default ordering for the order list view, ordered by
        `order_date` descending.
        search_fields (tuple): Fields that can be searched within the admin
        panel.
        list_filter (tuple): Fields by which the order list can be filtered.
    """
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

    search_fields = ('order_number', 'full_name', 'email',)


# Registering the Order model with the custom OrderAdmin configuration
admin.site.register(Order, OrderAdmin)
