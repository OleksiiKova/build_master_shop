from django import forms
from .models import UserProfile, Review


class UserProfileForm(forms.ModelForm):
    """
    A form for updating a user's profile information.

    This form is used to allow users to update their personal information,
    including
    full name, phone number, address, etc., in their profile.

    Methods:
        __init__(self, *args, **kwargs):
            Adds placeholders, classes, removes auto-generated labels, and
            sets autofocus on the first field.
    """
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes to the form fields, remove labels,
        and set autofocus on the first field (Full Name).
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_city': 'City',
            'default_county': 'County',
            'default_postcode': 'Postal Code',
        }

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False


class ReviewForm(forms.ModelForm):
    """
    A form for submitting a product review.

    This form is used by customers to submit a review for a product,
    including a rating and a comment. The form includes validation for the
    rating and comment fields.

    """
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
        }
