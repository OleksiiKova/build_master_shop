from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    A form for processing an Order.

    This form handles the creation or update of an Order, providing fields
    to collect essential customer and shipping information.

    Attributes:
        model (Order): The model that the form is based on.
        fields (tuple): The list of fields to be included in the form.
    """
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'city', 'county', 'postcode', 'country',
                  )

    def __init__(self, *args, **kwargs):
        """
        Customizes the form initialization by adding placeholders, setting
        autofocus, removing auto-generated labels, and adding custom classes
        to the form fields.

        This method is called when the form is created, and it modifies field
        attributes to make the form more user-friendly and stylized for
        front-end rendering (e.g., adding placeholders, custom classes, and
        autofocus).

        Args:
            *args: Additional arguments for the form initialization.
            **kwargs: Additional keyword arguments for the form initialization.
        """
        super().__init__(*args, **kwargs)

        # Dictionary for placeholders in form fields
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'city': 'City',
            'postcode': 'Postal Code',
            'county': 'County or State',
        }

        # Set autofocus on the 'full_name' field
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # Iterate through fields to customize their attributes
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
