from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from firebase_admin import credentials, auth, firestore
from google.auth.transport import requests
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
#from .forms import firestoreUserForm
from jeeimkg.db import get_firestore_client


def signup(request):
    return render(request, 'signup.html')
"""
@csrf_protect
def signup(request):
    form = firestoreUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)
"""

# vista para iniciar sesion

# Obtener el cliente Firestore
db = get_firestore_client()

@csrf_protect
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_ref = db.collection('users').where('email', '==', email).limit(1)
        user_docs = user_ref.get()
        if len(user_docs) == 0:
            # No se encontró un usuario con el email dado
            return render(request, 'login.html', {'error_message': 'Credenciales inválidas.'})
        user_doc = user_docs[0]
        if user_doc.get('password') == password:
            # Autenticación exitosa, inicia sesión en Django
            user, created = User.objects.get_or_create(email=email)
            user.set_password(password)
            user.save()
            django_user = authenticate(request, username=email, password=password)
            if django_user is not None:
                login(request, django_user)
                return redirect('adminsystem')
            else:
                return render(request, 'login.html', {'error_message': 'Credenciales inválidas.'})
        else:
            # Contraseña incorrecta
            return render(request, 'login.html', {'error_message': 'Credenciales inválidas.'})
    else:
        return render(request, 'login.html')

