from django.urls import path, include
from . import views

urlpatterns = [
    path('form_client/', views.starthere, name='inicia'),
]