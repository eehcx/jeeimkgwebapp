from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
#from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, user_passes_test
#from jeeimkg.decorators import firebase_auth_required
from auth_admin.views import firebase_auth_required

@firebase_auth_required
def sysadmin(request):
    return render(request, 'sysadmin.html', {})

def config(request):
    return render(request, 'configuration.html', {})

def profile(request):
    return render(request, 'profile.html')

def contactClient(request):
    return render(request, 'inbox.html', {})

def clients(request):
    return render(request, 'clients.html', {})

def employers(request):
    return render(request, 'employers.html', {})