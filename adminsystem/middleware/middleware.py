from firebase_admin import auth
from django.http import HttpResponseForbidden

class FirebaseAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Obtener el token de autenticación de la solicitud
        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[-1]

        # Verificar si el token es válido y obtener el ID de usuario asociado
        try:
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            request.user_id = uid
        except:
            return HttpResponseForbidden()

        response = self.get_response(request)

        return response

