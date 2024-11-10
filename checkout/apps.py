from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Configuration for the Checkout application.

    This class defines the configuration for the `checkout` application,
    including the automatic field type for primary keys and importing signals.

    Attributes:
        default_auto_field (str): The default field type for auto-incrementing
        primary keys.
        name (str): The name of the application in the Django project.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """
        Import signals when the app is ready.

        This method is called when the Django app is ready, and it imports
        the signals defined for the `checkout` app to ensure that they are
        connected and can handle the relevant events or actions.
        """
        import checkout.signals
