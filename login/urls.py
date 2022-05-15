from django.shortcuts import redirect
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('accounts/', include('allauth.urls')),
]