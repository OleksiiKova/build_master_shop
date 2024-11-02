from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """
    A form for users to send a contact message.

    This form allows users to enter their name, email, and a message.
    It is used for contact or support requests.

    Attributes:
        name (CharField): A field for the user's name.
        email (EmailField): A field for the user's email address.
        message (CharField): A field for the user's message.
    """
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'message',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
