from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .forms import SignUpForm

@csrf_protect

def signup(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)
"""
def register(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # registrar
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password2'])
                user.save()
                return HttpResponse('Usuario registrado')
            except:
                return HttpResponse('Usuario ya existe')
        return HttpResponse('Contraseñas no coinciden')
"""

# vista para iniciar sesion
@csrf_protect
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        return HttpResponse('Iniciar sesion')
