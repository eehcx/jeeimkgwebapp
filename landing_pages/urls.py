from django.urls import path, include, re_path
from . import views

urlpatterns = [
    #re_path(r'^.*$', views.mi_vista , name='inicio'),
    path('H8N1B3CJ5R7A9K0D2E6F4G8I3L9M2O5P1Q7S4U6W8Y0Z/', views.starthere, name='inicia'),
    path('GzoufrRRhZJS84Sz3b8U', views.employs, name='empleados'),
    path('form_client/finalized/', views.gracias, name='gracias'),
]