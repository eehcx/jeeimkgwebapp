from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
#from django.views.generic import TemplateView


def sysadmin(request):
    return render(request, 'sysadmin.html', {})

def config(request):
    return render(request, 'configuration.html', {})

def profile(request):
    return render(request, 'profile.html')

def contactClient(request):
    return render(request, 'inbox.html', {})