from django.urls import path
from . import views
from django.contrib.auth.models import User

urlpatterns = [
    path('perfil/', views.Perfil, name="perfil"),
    path('modificar-perfil/<int:pk>', views.UserUpdatePerfil.as_view(), name="modificar-perfil"),
    path('cambiar-contrasenia', views.cambiar_contrasenia, name="cambiar-contrasenia"),
    
]


