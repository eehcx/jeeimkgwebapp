from django.urls import path, include
from . import views

urlpatterns = [
    path('inicia/', views.starthere, name='inicia'),
]