from django.urls import path, include, re_path
from . import views

urlpatterns = [
    #re_path(r'^.*$', views.mi_vista , name='inicio'),
    path('form_client/', views.starthere, name='inicia'),
    path('GzoufrRRhZJS84Sz3b8U', views.employs, name='empleados'),
    path('form_client/finalized/', views.gracias, name='gracias'),
]