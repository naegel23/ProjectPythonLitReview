from django.apps import AppConfig


class TheblogConfig(AppConfig):
    name = 'theblog'

    def ready(self):
        from .signals import post_save_create_profile
