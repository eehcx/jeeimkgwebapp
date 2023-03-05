from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
import os, firebase_admin
from firebase_admin import credentials, auth, firestore, exceptions
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .forms import FirebaseSignupForm
from jeeimkg.db import get_firestore_client, credentials as db_credentials
from django.contrib import messages

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

def login(request):
    return render(request, 'login.html', {})
