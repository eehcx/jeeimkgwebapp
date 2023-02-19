from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
import os, firebase_admin
from firebase_admin import credentials, auth, firestore, exceptions
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
            # Crea un usuario en Authentication
            try:
                auth.create_user(
                    email=user.email,
                    password=user.password
                )
            except auth.AuthError as e:
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
            uid = user.uid
            # Create a custom token for the user
            custom_token = auth.create_custom_token(uid)
            # Add the token to the response
            response = redirect('adminsystem')
            response.set_cookie('session', custom_token)
            return response
        except exceptions.FirebaseError as e:
            # Handle any errors that occurred during authentication
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    return render(request, 'login.html')