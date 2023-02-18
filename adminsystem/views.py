from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
#from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

@login_required
def sysadmin(request):
    return render(request, 'sysadmin.html', {})

@login_required
def config(request):
    return render(request, 'configuration.html', {})

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def contactClient(request):
    return render(request, 'inbox.html', {})