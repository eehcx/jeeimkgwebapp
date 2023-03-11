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

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./jeeimkgServiceKey.json"
db = firestore.Client()
db = get_firestore_client()

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
#@csrf_exempt
#@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        firebase_token = request.POST.get('firebase_token')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            # redireccionamos al usuario a la página de inicio
            return HttpResponseRedirect('/adminsystem/') 
        else:
            return render(request, 'login.html', {'error_message': 'Error de autenticación con Firebase'})
    else:
        return render(request, 'login.html')