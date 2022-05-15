from django.db.models.base import Model
from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

urlpatterns = [

    path('crear-reserva/', views.crear_reserva, name="reservas"),
    path('mis-reservas/', views.mis_reservas, name='mis-reservas'),
    path('reservas/', views.reservas, name='todas-reservas'),
    path('eliminar-reserva/<int:id>', views.borrar_reserva, name='borrar-reserva'),
    path('crear-mesa/', views.crear_mesa, name="crear-mesa"),
    path('eliminar-mesa/<int:id>', views.eliminar_mesa, name="eliminar-mesa"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

handler404 = views.error404.as_view()