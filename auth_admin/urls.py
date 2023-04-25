from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('2FA/', views.two_factor_login, name='two_factor_login'),
    path('verify_phone_number/', views.verify_phone_number, name='verify_phone_number'),
    path('verify_code/', views.verify_code, name='verify_code'),
]