from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
#from .forms import startForm

@csrf_protect
def starthere(request):
    return render (request, 'inicia.html', {
        #'form': startForm()
    })
