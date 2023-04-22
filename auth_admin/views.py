from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
import os, firebase_admin, json, requests, pyrebase
from firebase_admin import credentials, auth as firebase_admin_auth, firestore, exceptions
from firebase_admin.exceptions import FirebaseError
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .forms import FirebaseSignupForm
from jeeimkg.db import get_firestore_client, credentials as db_credentials
from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from .decorators import require_authentication

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
        email = request.POST['email']
        password = request.POST['password']
        # Send the email and password to Firebase Authentication
        
        user = auth.sign_in_with_email_and_password(email, password)
        #print(user)
        id_token = user['idToken']
        decoded_token = firebase_admin_auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        # Log in the user using the uid
        # ...
        # Redirect the user to the adminsystem view
        return redirect('adminsystem')
    return render(request, 'login.html')