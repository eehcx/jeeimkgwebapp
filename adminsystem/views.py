from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required, user_passes_test

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