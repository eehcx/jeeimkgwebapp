from django.apps import AppConfig
from .middleware import FirebaseAuthenticationMiddleware

class AdminsystemConfig(AppConfig):
    name = 'adminsystem'

    def ready(self):
        # Agrega el middleware a la configuración de la aplicación
        self.middleware.append(FirebaseAuthenticationMiddleware)

