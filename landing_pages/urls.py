from django.urls import path, include
from . import views

urlpatterns = [
    #path('<str:code>/', views.starthere, name='inicia'),
    path('form_client/', views.starthere, name='inicia'),
    #path('invalid_code/', views.invalid_code, name='invalid_code'),
]