from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """
    Configuration class for the 'products' Django app.

    Attributes:
        default_auto_field (str): Specifies the default field type for
        automatically generated primary keys. In this case, it is set to
        BigAutoField.
        
        name (str): The full Python path to the application, which helps Django
        identify the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
