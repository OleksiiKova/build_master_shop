from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    """
    Form for creating or updating a BlogPost.

    This form is based on the BlogPost model and includes fields for
    the title, content, and an image. It is used for handling form
    submissions in views related to the BlogPost model.

    Attributes:
        model (class): The model that this form is associated with (BlogPost).
        fields (list): The fields from the model that will be included in the
        form.
    """
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image']
