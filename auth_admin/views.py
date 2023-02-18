from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
import os
from firebase_admin import credentials, auth, firestore
from google.auth.transport import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .forms import SignupForm
from .models import User
from jeeimkg.db import get_firestore_client, credentials as db_credentials
from django.contrib import messages

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

            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# vista para iniciar sesion
@csrf_protect
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') # redirige a la página de inicio después del inicio de sesión exitoso
        else:
            messages.error(request, 'Credenciales inválidas') # muestra un mensaje de error en la página si las credenciales no son válidas

    return render(request, 'login.html')