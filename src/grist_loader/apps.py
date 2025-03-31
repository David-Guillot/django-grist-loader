from django.apps import AppConfig


class GristConfig(AppConfig):
    name = "grist_loader"

    def ready(self):
        """Autodiscover documents and register signals."""
        self.module.autodiscover()
