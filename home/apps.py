from django.apps import AppConfig


# Define the configuration class for the 'home' application
class HomeConfig(AppConfig):
    # Set the default primary key field type for models in this application
    default_auto_field = 'django.db.models.BigAutoField'
    # Specify the name of the application
    name = 'home'
