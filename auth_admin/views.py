from django.shortcuts import render, redirect
import os, firebase_admin, json, requests, pyrebase, pyotp
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .forms import FirebaseSignupForm
from jeeimkg.db import get_firestore_client, credentials as db_credentials
from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from firebase_admin import auth as firebase_admin_auth, credentials,  firestore, exceptions
from firebase_admin.exceptions import FirebaseError

config = {
            "apiKey": "AIzaSyBXEiXDLhTkwYUCVD4oANFZeMtzqEoPLls",
            "authDomain": "jeeimkg-5705b.firebaseapp.com",
            "databaseURL": "https://jeeimkg-5705b-default-rtdb.firebaseio.com/",
            "storageBucket": "jeeimkg-5705b.appspot.com"
        }

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

"""| Vista que me crea usuarios apartir de mi Formulario |"""
@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = FirebaseSignupForm(request.POST)
        if form.is_valid():
            form.signup()
            return redirect('login')
    else:
        form = FirebaseSignupForm()
    return render(request, 'signup.html', {'form': form})

@csrf_protect
def login(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']
            user = auth.sign_in_with_email_and_password(email, password)
            id_token = user['idToken']
            decoded_token = firebase_admin_auth.verify_id_token(id_token)
            uid = decoded_token['uid']
            #
            request.session['email'] = email

            # Redirecciona a la vista de adminsystem
            return redirect('adminsystem')
        except:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    try:
        del request.session['email']
    except:
        pass
    return redirect('login')


"""| Autentificación de dos factores |"""


def two_factor_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            # Autentica al usuario en Firebase
            user = auth.sign_in_with_email_and_password(email, password)
            # Verifica si el usuario tiene habilitado el inicio de sesión de dos factores
            if not user['emailVerified']:
                # Si el correo electrónico no ha sido verificado, envía un correo de verificación
                auth.send_email_verification(user['idToken'])
                messages.warning(request, 'Por favor, verifica tu correo electrónico antes de iniciar sesión.')
                return redirect('index') #two_factor_login
            elif not user['multiFactor']['enrolledFactors']:
                # Si el usuario no tiene habilitado el inicio de sesión de dos factores, redirige a la vista de inicio de sesión normal
                auth.send_email_verification(user['idToken'])
                messages.warning(request, 'Por favor, habilita el inicio de sesión de dos factores antes de iniciar sesión.')
                return redirect('login')
            else:
                # Si el usuario está habilitado para el inicio de sesión de dos factores, solicita su número de teléfono
                request.session['user_id'] = user['localId']
                return redirect('verify_phone_number')
        except:
            messages.error(request, 'Correo electrónico o contraseña incorrectos')
            return redirect('two_factor_login')
    return render(request, 'two_factor_login.html')

"""
def send_verification_code(phone_number):
    settings = firebase_admin_auth.ApplicationVerifierSettings(
        app_verification_disabled_for_testing=True
    )
    provider = firebase_admin_auth.PhoneAuthProvider(settings=settings)
    verification_id = provider.generate_verification_id(phone_number)
    message = 'Tu código de verificación de inicio de sesión de dos factores es {}'.format(verification_id)
    # Enviar el mensaje con el código de verificación al número de teléfono
    return verification_id
"""

def verify_phone_number(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        session_id = request.session['user_id']
        # Genera un código de verificación y envía el mensaje de texto al número de teléfono del usuario
        verification_code = pyotp.TOTP('base32secret3232').now()
        auth.create_session_cookie(user_id=session_id, phone_number=phone_number, verification_code=verification_code)
        return redirect('verify_code')
    return render(request, 'verify_phone_number.html')

def verify_code(request):
    if request.method == 'POST':
        verification_code = request.POST['verification_code']
        try:
            # Recupera el usuario de Firebase con la sesión actual
            session_cookie = request.COOKIES.get('session')
            decoded_claims = auth.verify_session_cookie(session_cookie, check_revoked=True)
            user = auth.get_user(decoded_claims['uid'])
            # Verifica el código de verificación ingresado
            auth.multi_factor.session_cookie_verifier(session_cookie, verification_code)
            # Si el código es válido, autentica al usuario en Django
            messages.success(request, 'Inicio de sesión exitoso')
            return redirect('home')
        except:
            messages.error(request, 'Código de verificación incorrecto')
            return redirect('verify_code')
    return render(request, 'verify_code.html')