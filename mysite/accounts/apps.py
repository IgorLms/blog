from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    verbose_name = 'Аккаунт'

    def ready(self):
        """Предопределение метода ready"""

        import accounts.signals
