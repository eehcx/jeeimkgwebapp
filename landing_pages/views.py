from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string
from .forms import ClientForm
#from .models import UniqueCode
from firebase_admin import firestore # si falla el registro añadir el import firebase_Admin
import os

# VARIABLES DE ENTORNO FIRESTORE
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./jeeimkgServiceKey.json"
db = firestore.Client()

# URL UNICA POR CADA USUARIO
"""   
def generate_unique_code():
    code = get_random_string(length=36)
    try:
        code_obj = UniqueCode.objects.create(code=code)
        code_obj.save()
        return code
    except InterruptedError:
        return generate_unique_code()

def landing_page(request, code):
    try:
        UniqueCode.objects.get(code=code)
        return render(request, 'inicia.html')
    except UniqueCode.DoesNotExist:
        return redirect('invalid_code')

def send_code_to_user(email):
    unique_code = generate_unique_code()
    # Enviar el código único al usuario a través de correo electrónico

def invalid_code(request):
    return render(request, 'invalid_code.html') 
"""
# FORMULARIO DE REGISTRO DE NUEVOS CLIENTES
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

        # Crear un coleccion con los datos
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
    

def employs(request):
    return render(request, 'employs.html')