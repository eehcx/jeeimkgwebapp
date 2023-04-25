from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import user_passes_test
from .forms import EditCustomerForm
import os, firebase_admin, requests, pyrebase
from firebase_admin import credentials, firestore, db
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from auth_admin.decorators import firebase_login_required

config = {
    "apiKey": "AIzaSyBXEiXDLhTkwYUCVD4oANFZeMtzqEoPLls",
    "authDomain": "jeeimkg-5705b.firebaseapp.com",
    "databaseURL": "https://jeeimkg-5705b-default-rtdb.firebaseio.com/",
    "storageBucket": "jeeimkg-5705b.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

@firebase_login_required
def sysadmin(request):
    email = request.session.get('email')
    # Obtener todos los datos de la colección "Customers" en orden inverso
    customers = db.child("Customers").get().val()
    customers = list(customers.values())

    # Obtener todos los datos de la colección "contacts"
    contacts = db.child("contacts").get().val()
    contacts = list(contacts.values())

    pre_customers = db.child("Pre-Customers").get().val()
    pre_customers = list(pre_customers.values())

    # Invierte el orden de los datos en la lista
    customers_data = list(reversed(customers))[:15]
    contacts_data = list(reversed(contacts))[:15]
    pre_customers_data = list(reversed(pre_customers))[:15]

    context = {
        'customers_data': customers_data,
        'contacts_data': contacts_data,
        'pre_customers_data': pre_customers_data,
        'email': email
    }

    return render(request, 'sysadmin.html', context)

@firebase_login_required
def config(request):
    return render(request, 'configuration.html', {})

@firebase_login_required
@csrf_protect
def profile(request):
    email = request.session.get('email')

    context = {
        'email': email
    }

    return render(request, 'profile.html', context)

@firebase_login_required
def contactClient(request, start=0, end=10):
    email = request.session.get('email')

    # Obtener todos los datos de la colección "Pre-Customers"
    pre_customers = db.child("Pre-Customers").get()
    
    # Crear una lista para almacenar los datos de los clientes
    pre_customers_data = []

    for pre_customer in pre_customers.each():
        data = pre_customer.val()
        data['id'] = pre_customer.key()
        pre_customers_data.append(data)

    # Invertir la lista de datos de los clientes
    pre_customers_data.reverse()

    context = {
        #'contacts': contacts,
        'pre_customers_data': pre_customers_data[start:end],
        'start': start,
        'end': end,
        'email': email
    }

    return render(request, 'inbox.html', context)

@firebase_login_required
def deletePreCustomer(request, pre_customer_id):
    # Eliminar el pre-customer de la base de datos
    db.child("Pre-Customers").child(pre_customer_id).remove()

    # Redireccionar a la página de listado de pre-customers
    return redirect('contactClient')


def edit_contact(request, pre_customers_id):
    # Obtener los datos del cliente a partir de su ID
    contact = db.child("Pre-Customers").child(pre_customers_id).get().val()

    # Imprimir los datos del cliente en la consola
    #print(customer)

    # Pasar los datos del cliente al contexto
    context = {
        'contact': contact,
        'pre_customers_id': pre_customers_id
    }

    # Renderizar el template con el contexto
    return render(request, 'edit_contact.html', context)

@firebase_login_required
def clients(request, start=0, end=10):
    email = request.session.get('email')
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
        'end': end,
        'email': email
    }

    return render(request, 'clients.html', context)

@firebase_login_required
def edit_customer(request, customer_id):
    # Obtener los datos del cliente a partir de su ID
    customer = db.child("Customers").child(customer_id).get().val()

    # Imprimir los datos del cliente en la consola
    #print(customer)

    # Pasar los datos del cliente al contexto
    context = {
        'customer': customer,
        'customer_id': customer_id
    }

    # Renderizar el template con el contexto
    return render(request, 'edit_customer.html', context)

@firebase_login_required
def update_customer(request, customer_id):
    # Obtener los datos del cliente a partir de su ID
    customer = db.child("Customers").child(customer_id).get().val()

    if request.method == 'POST':
        # Obtener los nuevos datos del cliente del formulario de actualización
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phoneNumber')
        service = request.POST.get('service')
        income = request.POST.get('income')
        address = request.POST.get('address')
        sector = request.POST.get('sector')
        businessType = request.POST.get('businessType')
        niche = request.POST.get('niche')
        areaOfInterest = request.POST.get('areaOfInterest')
        budget = request.POST.get('budget')
        time = request.POST.get('time')

        # Actualizar los datos del cliente en Firebase Realtime Database
        data = {
            'name': name,
            'email': email,
            'phoneNumber': phoneNumber,
            'service': service,
            'income': income,
            'address': address,
            'sector': sector,
            'businessType': businessType,
            'niche': niche,
            'areaOfInterest': areaOfInterest,
            'budget': budget,
            'time': time
        }
        db.child("Customers").child(customer_id).update(data)

        # Redirigir al usuario a la página de detalles del cliente actualizado
        return redirect('edit_customer', customer_id=customer_id)

    # Si el formulario no es válido o si es una solicitud GET, renderizar el template con los datos del cliente
    context = {
        'customer': customer,
        'customer_id': customer_id
    }
    return render(request, 'edit_customer.html', context)

@firebase_login_required
def employers(request):
    return render(request, 'employers.html', {})

@firebase_login_required
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