from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('acerca/', views.about, name='acerca'),
    path('contacto/', views.contact, name='contacto'),
    path('clientes/',views.clientes, name='clientes'),
    path('fundacion/',views.fundation, name='fundacion'),
    path('productos/',views.products, name='productos'),
    path('conferencias/',views.conferencias, name='conferencias'),
    path('afiliacion/', views.afiliacion, name='afiliacion'),
    path('mapa/', views.mapa, name="mapa"),
    path('terminos/',views.terminos, name='terminos'),
    path('privacidad/',views.privacity, name='privacidad')
]