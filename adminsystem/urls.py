from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.sysadmin, name='adminsystem'),
    path('configuration/',views.config, name='configuration'),
    path('profile/',views.profile, name='profile'),
    path('inbox/',views.contactClient, name='contactClient'),
    path('clients/',views.clients, name='clients'),
    path('employers/',views.employers, name='employers')
]