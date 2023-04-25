from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string
from .forms import ClientForm
import firebase_admin, requests, pyrebase, os
from firebase_admin import firestore # si falla el registro añadir el import firebase_Admin

config = {
    "apiKey": "AIzaSyBXEiXDLhTkwYUCVD4oANFZeMtzqEoPLls",
    "authDomain": "jeeimkg-5705b.firebaseapp.com",
    "databaseURL": "https://jeeimkg-5705b-default-rtdb.firebaseio.com/",
    "storageBucket": "jeeimkg-5705b.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


def mi_vista(request):
    # Recuperar todos los documentos de la colección "urls"
    documentos = db.child("urls").get().val()

    # Verificar si alguno de los documentos contiene un código válido
    código_válido = False
    for doc_id, doc_data in documentos.items():
        if "code" in doc_data and "used" in doc_data:
            if doc_data["used"] == False and request.path == doc_data["code"]:
                código_válido = True
                break

    if código_válido:
        # Si se proporcionó un código válido, renderizar la vista
        return render(request, 'pruebas.html')
    else:
        # Si no se proporcionó un código válido, mostrar un mensaje de error
        return HttpResponse('Código no válido')

# FORMULARIO DE REGISTRO DE NUEVOS CLIENTES
@csrf_protect
def starthere(request):
    form = ClientForm(request.POST)
    if form.is_valid():
        # Obtener los datos del formulario
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phoneNumber = form.cleaned_data['phoneNumber']
        sector = form.cleaned_data['sector']
        service = form.cleaned_data['service']
        redes_sociales1 = form.cleaned_data.get('redes_sociales1', [])
        redes_sociales2 = form.cleaned_data.get('redes_sociales2', [])
        socialMedia = redes_sociales1 + redes_sociales2
        income = form.cleaned_data['income']
        address = form.cleaned_data['address']
        needs = form.cleaned_data['needs']
        businessType = form.cleaned_data['businessType']
        niche = form.cleaned_data['niche']
        businessSize = form.cleaned_data['businessSize'] 
        goals = form.cleaned_data['goals']
        areaOfInterest = form.cleaned_data['areaOfInterest']
        budget = form.cleaned_data['budget']
        time = form.cleaned_data['time']

        # Crear un diccionario con los datos del formulario
        datos_empresa = {
            'name': name,
            'email': email,
            'phoneNumber': phoneNumber,
            'sector': sector,
            'service': service,
            'socialMedia': socialMedia,
            'income': income,
            'address': address,
            'needs': needs,
            'businessType': businessType,
            'niche': niche,
            'businessSize': businessSize,
            'goals': goals,
            'areaOfInterest': areaOfInterest,
            'budget': budget,
            'time': time
        }

        # Hacer una solicitud POST a tu API REST con los datos del formulario
        url = 'http://localhost:4000/customers'
        response = requests.post(url, json=datos_empresa)

        if response.ok:
            # Si la solicitud fue exitosa, redirigir a la página de confirmación
            return redirect('gracias')
        else:
            # Si la solicitud falló, renderizar la plantilla del formulario con errores
            form.add_error(None, 'Error al guardar los datos. Por favor intenta de nuevo.')
            return render(request, 'inicia.html', {'form': form})
    else:
        # Si el formulario no es válido, renderizar la plantilla del formulario con errores
        return render(request, 'inicia.html', {'form': form})
    

def employs(request):
    return render(request, 'employs.html')


def gracias(request):
    return render(request, 'gracias.html')