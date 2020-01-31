from django.apps import AppConfig


class PublishersConfig(AppConfig):
    name = 'publishers'

    def ready(self):
        import publishers.signals