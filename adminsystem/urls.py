from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.sysadmin, name='adminsystem'),
    path('configuration/',views.config, name='configuration'),
    path('profile/',views.profile, name='profile'),
    path('inbox/',views.contactClient, name='contactClient'),
    path('clients/',views.clients, name='clients'),
    path('clients/<int:start>/<int:end>/', views.clients, name='clients'),
    path('clients/edit/<str:customer_id>/', views.edit_customer, name='edit_customer'),
    path('administration/clients/update/<str:customer_id>/', views.update_customer, name='update_customer'),
    path('employers/',views.employers, name='employers'),
    path('search/', views.search, name='search')
]