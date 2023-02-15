from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('administration/', include('adminsystem.urls')),
    path('', include('authentication.urls')),
    path('landing/', include('landing_pages.urls')),
    path('', include('home.urls'))
]
