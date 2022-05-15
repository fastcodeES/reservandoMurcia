from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('contacto/', views.contacto, name='contacto'),
    path('mensajes/', views.mensajes, name='mensajes'),
    path('respuestas/<str:email>', views.respuestas, name='respuestas'),
    path('borrar-mensaje/<id>', views.borrar_mensaje, name='borrar-mensaje'),
]