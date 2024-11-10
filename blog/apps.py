from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configuration for the 'blog' app.

    This class specifies the default primary key field type and the name of
    the application within the Django project.

    Attributes:
        default_auto_field (str): Specifies the type of primary key field
        to use.
        name (str): The name of the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
