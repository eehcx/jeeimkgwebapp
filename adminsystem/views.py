from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import user_passes_test
from .forms import EditCustomerForm
import os, firebase_admin, requests, pyrebase
from firebase_admin import credentials, firestore, db
from django.http import HttpResponse
from django.contrib import messages
from auth_admin.decorators import firebase_login_required

config = {
    "apiKey": "AIzaSyBXEiXDLhTkwYUCVD4oANFZeMtzqEoPLls",
    "authDomain": "jeeimkg-5705b.firebaseapp.com",
    "databaseURL": "https://jeeimkg-5705b-default-rtdb.firebaseio.com/",
    "storageBucket": "jeeimkg-5705b.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

#@firebase_login_required
def sysadmin(request):

    customers = db.child("Customers").get().val()
    customers = list(customers.values())

    pre_customers = db.child("Pre-Customers").get().val()
    pre_customers = list(pre_customers.values())

    # Invierte el orden de los datos en la lista
    customers_data = list(reversed(customers))[:15]
    pre_customers_data = list(reversed(pre_customers))[:15]

    context = {
        'customers_data': customers_data,
        'pre_customers_data': pre_customers_data,
    }

    return render(request, 'sysadmin.html', context)

def config(request):
    return render(request, 'configuration.html', {})

def profile(request):
    return render(request, 'profile.html')

def contactClient(request):
    # Obtener todos los datos de la colección "Customers" en orden inverso
    customers = db.child("Customers").get().val()
    customers = list(customers.values())[::-1]

    """
    # Obtener todos los datos de la colección "Contacts"
    contacts = db.child("contacts").get().val()
    contacts = list(contacts.values())
    """

    # Obtener todos los datos de la colección "Pre-Customers"
    pre_customers = db.child("Pre-Customers").get().val()
    pre_customers = list(pre_customers.values())

    # Crear una lista para almacenar los nombres de los últimos 4 clientes
    last_customers = []

    # Iterar sobre los últimos 4 clientes y agregar sus nombres a la lista
    for i in range(4):
        if i >= len(customers):
            break
        last_customers.append(customers[i]['name'])

    # Pasar los nombres de los últimos 4 clientes, los datos de la colección "Contacts" y los datos de la colección "Pre-Customers" al contexto
    context = {
        'last_customers': last_customers,
        #'contacts': contacts,
        'pre_customers': pre_customers
    }

    return render(request, 'inbox.html', context)

def clients(request, start=0, end=10):
    # Obtener todos los datos de la colección "Customers"
    customers = db.child("Customers").get()

    # Crear una lista para almacenar los datos de los clientes
    client_data = []

    # Iterar sobre los datos obtenidos y agregarlos a la lista
    for customer in customers.each():
        data = customer.val()
        data['id'] = customer.key()
        client_data.append(data)

    # Invertir la lista de datos de los clientes
    client_data.reverse()

    # Pasar los datos de los clientes al contexto para que se puedan renderizar en el template
    context = {
        'client_data': client_data[start:end],
        'start': start,
        'end': end
    }

    return render(request, 'clients.html', context)

def edit_customer(request, customer_id):
    
    # Verificar si la solicitud es POST
    if request.method == 'POST':
        # Obtener los datos del formulario
        data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phoneNumber': request.POST['phoneNumber'],
            'sector': request.POST['sector'],
            'service': request.POST['service'],
            'socialMedia': request.POST['social'],
            'income': request.POST['income'],
            'address': request.POST['address'],
            'needs': request.POST['needs'],
            'businessType': request.POST['businessType']
        }

        # Actualizar los datos del cliente en la base de datos de Firebase
        db.child('Customers').child(customer_id).update(data)

        # Redirigir al usuario a la página de detalles del cliente
        return redirect('clients', {})

    # Obtener los datos del cliente a partir de su ID
    customer = db.child("Customers").child(customer_id).get().val()

    # Imprimir los datos del cliente en la consola
    #print(customer)

    form = EditCustomerForm(customer)

    # Pasar los datos del cliente al contexto
    context = {
        'customer': customer,
        'customer_id': customer_id,
    }

    # Renderizar el template con el contexto
    return render(request, 'edit_customer.html', context)


def update_customer(request, customer_id):
    # Obtener los datos del cliente a partir de su ID
    customer = db.child("Customers").child(customer_id).get().val()

    # Imprimir los datos del cliente en la consola
    #print(customer)

    form = EditCustomerForm(request.POST, instance=customer)

    # Si el formulario es válido, actualizar los datos del cliente
    if form.is_valid():
        form.save()
        messages.success(request, 'Cliente actualizado correctamente')
        return redirect('clients')

    # Si el formulario no es válido, renderizar el template con los datos del cliente
    context = {
        'customer': customer,
        'customer_id': customer_id,
    }

    return render(request, 'edit_customer.html', context)


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