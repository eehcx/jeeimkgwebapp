from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .forms import ClientForm
from firebase_admin import firestore
import os, firebase_admin

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./jeeimkgServiceKey.json"
db = firestore.Client()

@csrf_protect
def starthere(request):
    form = ClientForm(request.POST)
    if form.is_valid():
        # Obtener los datos del formulario
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        telefono = form.cleaned_data['telefono']
        sector = form.cleaned_data['sector']
        servicio = form.cleaned_data['servicio']
        #redes_sociales = form.cleaned_data['redes_sociales']
        redes_sociales1 = form.cleaned_data.get('redes_sociales1', [])
        redes_sociales2 = form.cleaned_data.get('redes_sociales2', [])
        redes_sociales = redes_sociales1 + redes_sociales2
        ingresos = form.cleaned_data['ingresos']
        direccion = form.cleaned_data['direccion']
        necesidades = form.cleaned_data['necesidades']

        # Crear un diccionario con los datos
        datos_empresa = {
            'nombre': nombre,
            'email': email,
            'telefono': telefono,
            'sector': sector,
            'servicio': servicio,
            'redes_sociales': redes_sociales,
            'ingresos': ingresos,
            'direccion': direccion,
            'necesidades': necesidades,
        }

        # Guardar los datos en Firestore
        db.collection('clients').add(datos_empresa)

        # Renderizar la plantilla de confirmación
        return redirect('index')
    else:
        print(form.errors)
        # Renderizar la plantilla del formulario con errores
        return render(request, 'inicia.html', {'form': form})
