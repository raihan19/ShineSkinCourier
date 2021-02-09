from django.apps import AppConfig


class RegistrationuserConfig(AppConfig):
    name = 'registrationUser'

    def ready(self):
        import registrationUser.signals
