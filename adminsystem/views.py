from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
#from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

def sysadmin(request):
    #validame la sesion apartir del login hecho
    return render(request, 'sysadmin.html', {})

def config(request):
    return render(request, 'configuration.html', {})

def profile(request):
    return render(request, 'profile.html')

def contactClient(request):
    return render(request, 'inbox.html', {})