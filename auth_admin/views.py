from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
import os, firebase_admin, json, requests
from firebase_admin import credentials, auth, firestore, exceptions
from firebase_admin.exceptions import FirebaseError
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .forms import FirebaseSignupForm
from jeeimkg.db import get_firestore_client, credentials as db_credentials
from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods

#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./jeeimkgServiceKey.json"
#db = firestore.Client()
#db = get_firestore_client()

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
        # Obtener los datos del formulario
        email = request.POST['email']
        password = request.POST['password']

        # Hacer la solicitud a la API de login
        response = requests.post('https://restapi-jeeimkg.onrender.com/login', json={'email': email, 'password': password})

        # Verificar la respuesta de la API
        if response.status_code == 200:
            message = 'Inicio de sesión exitoso'
        elif response.status_code == 401:
            message = 'Contraseña incorrecta'
        else:
            message = 'Usuario no encontrado'

        # Renderizar la plantilla con el mensaje de respuesta
        return render(request, 'login.html', {'message': message})

    # Si la solicitud no es POST, renderizar el formulario de login
    return render(request, 'login.html')