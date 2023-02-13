from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

def home(request):
    return HttpResponse("This is home page")

def index(request):
    return render(request, 'index.html', {})

@csrf_protect
def contact(request):
    return render (request, 'contact.html', {})

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
