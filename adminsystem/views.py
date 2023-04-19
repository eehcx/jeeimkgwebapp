import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required, user_passes_test
from googleapiclient.discovery import build
from .models import Cliente
import firebase_admin, requests, pyrebase
from firebase_admin import credentials, firestore

config = {
    "apiKey": "AIzaSyBXEiXDLhTkwYUCVD4oANFZeMtzqEoPLls",
    "authDomain": "jeeimkg-5705b.firebaseapp.com",
    "databaseURL": "https://jeeimkg-5705b-default-rtdb.firebaseio.com/",
    "storageBucket": "jeeimkg-5705b.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

"""
def get_data_from_api():
    url = 'https://restapi-jeeimkg.onrender.com/customers'
    #headers = {'Authorization': 'Bearer <token_de_autenticación>'}
    
    clientes = Cliente.objects.all()  # Obtener todos los clientes
    
    params = {}
    for cliente in clientes:
        params[cliente.name] = cliente.name
        params[cliente.phoneNumber] = cliente.phoneNumber
        params[cliente.service] = cliente.service
        params[cliente.businessSize] = cliente.businessSize
        params[cliente.niche] = cliente.niche
        params[cliente.businessType] = cliente.businessType
        params[cliente.email] = cliente.email
    
    response = requests.get(url, params=params) #, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
"""


def sysadmin(request):
    return render(request, 'sysadmin.html', {})

def config(request):
    return render(request, 'configuration.html', {})

def profile(request):
    return render(request, 'profile.html')

def contactClient(request):
    return render(request, 'inbox.html', {})

def clients(request):
    # Obtener todos los datos de la colección "Customers"
    customers = db.child("Customers").get()

    # Crear una lista para almacenar los datos de los clientes
    client_data = []

    # Iterar sobre los datos obtenidos y agregarlos a la lista
    for customer in customers.each():
        client_data.append(customer.val())

    # Pasar los datos de los clientes al contexto para que se puedan renderizar en el template
    context = {
        'client_data': client_data
    }

    # Agregar esta línea para imprimir los datos en la consola
    print(client_data)

    return render(request, 'clients.html', context)


"""
def clients(request):
    data = get_data_from_api()
    
    if data:
        # Procesar los datos y hacer lo que necesites con ellos
        return render(request, 'clients.html', {'data': data})
    else:
        # Si no se pudieron obtener los datos, mostrar un error
        return render(request, 'error_template.html')
"""


def employers(request):
    return render(request, 'employers.html', {})

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        templates_dir = os.path.join(settings.BASE_DIR, 'templates')
        for root, dirs, files in os.walk(templates_dir):
            for file in files:
                if file.endswith('.html') and query.lower() in file.lower():
                    results.append(os.path.join(root, file))
    return render(request, 'search_results.html', {'results': results})