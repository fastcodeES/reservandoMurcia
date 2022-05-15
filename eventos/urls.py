from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('ver-evento/<pk>/', views.ver_evento.as_view(), name='ver-evento'),
    path('eliminar-evento/<int:id>/', views.eliminar_eventos, name='eliminar-evento'),
    path('crear-evento/', views.crear_evento, name="crear-evento"),
    path('guardar-evento/', views.guardar_evento, name="guardar-evento"),
]
