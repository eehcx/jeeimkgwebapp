from django.shortcuts import render, redirect
from django.http import HttpResponse
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
            form.save()  # Guarda el modelo Contact en la base de datos de Django y en Firestore.
            return redirect('index')
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
