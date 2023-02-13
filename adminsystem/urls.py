from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('administration/',views.sysadmin, name='adminsystem'),
    path('configuration/',views.config, name='configuration'),
    path('profile/',views.profile, name='profile'),
    path('inbox/',views.contactClient, name='contactClient'),
]