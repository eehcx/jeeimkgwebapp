from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
import os
import firebase_admin
from firebase_admin import credentials, auth, firestore, exceptions
from django.contrib.auth.decorators import login_required
from google.auth.transport import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .forms import SignupForm
from .models import User
from functools import wraps
from jeeimkg.db import get_firestore_client, credentials as db_credentials
from django.contrib import messages
from urllib.parse import urlparse

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./jeeimkgServiceKey.json"
db = firestore.Client()
db = get_firestore_client()

# vista para crear usuario
@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Crea un nuevo objeto User con los datos del formulario
            user = User(email=form.cleaned_data['email'],
                        password=form.cleaned_data['password'])
            # Guarda el objeto User en la base de datos de Django y en Firestore
            user.save()
            # Crea un usuario en Authentication
            try:
                auth.create_user(
                    email=user.email,
                    password=user.password
                )
            except exceptions.FirebaseError as e:
                # Maneja el error aquí
                pass
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# vista para iniciar sesion
@csrf_protect
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = auth.get_user_by_email(email)
            user = authenticate(request, uid=user.uid, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Incorrect email or password.')
        except auth.AuthError as e:
            messages.error(request, str(e))
    return render(request, 'login.html')

# funcion para verificar si el usuario esta autenticado
def firebase_auth_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        session_cookie = request.COOKIES.get('session')
        if not session_cookie:
            return redirect(f'/login/?next={request.path}')
        try:
            decoded_claims = auth.verify_session_cookie(session_cookie, check_revoked=True)
            uid = decoded_claims['uid']
            request.user = auth.get_user(uid)
            # get user object from Firebase Auth
            user = auth.get_user(uid)
            # sign in user on client side
            auth.auth().signInWithEmailAndPassword(user.email, 'password')
        except auth.InvalidSessionCookieError:
            return redirect(f'/login/?next={request.path}')
        except auth.RevokedIdTokenError:
            return redirect(f'/login/?next={request.path}')
        response = view_func(request, *args, **kwargs)
        if response.status_code == 302 and 'Location' in response:
            # If the view returned a redirect response, check if the
            # redirect location is to the login page, and if so, add
            # the 'next' parameter to the URL.
            login_url = urlparse(reverse('login'))
            redirect_url = urlparse(response['Location'])
            if login_url.path == redirect_url.path:
                redirect_url = redirect_url._replace(query=f'next={request.path}')
                response['Location'] = redirect_url.geturl()
        return response
    return wrapped_view

