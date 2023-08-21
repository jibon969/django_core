from django.apps import AppConfig


class AbstractModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'abstract_model'
