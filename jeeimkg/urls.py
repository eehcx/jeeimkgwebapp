from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('administration/', include('adminsystem.urls')),
    path('', include('auth_admin.urls')),
    path('landing/', include('landing_pages.urls')),
    path('', include('home.urls'))
]
