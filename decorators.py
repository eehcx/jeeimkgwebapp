from google.auth.transport import requests
from google.oauth2.id_token import verify_oauth2_token
from django.http import JsonResponse
import os, firebase_admin
from firebase_admin import auth, credentials, firestore
from jeeimkg.db import get_firestore_client, credentials as db_credentials

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./jeeimkgServiceKey.json"
db = firestore.Client()
db = get_firestore_client()

# Firebase Auth Decorator
def firebase_auth_required(func):
    def wrapper(request, *args, **kwargs):
        id_token = request.META.get('HTTP_AUTHORIZATION', None)

        if id_token is None:
            return JsonResponse({'error': 'No se ha proporcionado un token de autenticación.'}, status=401)

        try:
            # Verifica la validez del token de autenticación de Firebase
            decoded_token = auth.verify_id_token(id_token, check_revoked=True)
            # Obtén el UID del usuario autenticado
            uid = decoded_token['uid']
            # Verifica que el usuario exista en Firebase Authentication
            user = auth.get_user(uid)
            # Verifica que el usuario esté autenticado con Google
            if 'google.com' not in user.provider_data[0]['providerId']:
                raise ValueError('Token de autenticación no emitido por Google.')

            # Agrega la información del usuario a la sesión
            request.session['uid'] = uid
            request.session['email'] = user.email

            # Si la autenticación ha sido exitosa, se ejecuta la vista
            return func(request, *args, **kwargs)

        except ValueError as e:
            # En caso de que el token no sea válido o el usuario no esté autenticado, devuelve un error 401
            return JsonResponse({'error': 'Token de autenticación no válido: {}'.format(e)}, status=401)

    return wrapper
