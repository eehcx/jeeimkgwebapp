from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('adminsystem.urls')),
    path('', include('authentication.urls')),
    path('', include('landing_pages.urls')),
    path('', include('home.urls'))
]
