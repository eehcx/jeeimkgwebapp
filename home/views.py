from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_protect
from .forms import ContactForm

def home(request):
    return HttpResponse("This is home page")

def index(request):
    return render(request, 'index.html', {})

@csrf_protect
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Realiza una solicitud POST a la API REST para guardar los datos de contacto
            response = requests.post('http://localhost:3000/contacts', json=form.cleaned_data)
            
            if response.status_code == 200:
                return redirect('index')
            else:
                form.add_error(None, 'Hubo un error al enviar el mensaje. Por favor inténtalo de nuevo.')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def about(request):
    return render(request,'acerca.html')

def fundation(request):
    return render(request,'fundation.html')

def clientes(request):
    return render(request,'clientes.html')

def products(request):
    return render(request,'products.html')

def conferencias(request):
    return render(request, 'conferencias.html')

def afiliacion(request):
    return render(request, 'afiliacion.html')

def mapa(request):
    return render(request, 'mapa.html')

def terminos(request):
    return render(request, 'terminos.html')

def privacity(request):
    return render(request, 'privacidad.html')

def aviso(request):
    return render(request, 'aviso.html')

def work(request):
    return render(request, 'work.html')

def opinions(request):
    return render(request, 'opinions.html')
