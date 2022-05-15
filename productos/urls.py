from django.urls import path

from productos import views


urlpatterns = [
    path('crear-producto/', views.crear_producto, name="crear-producto"),
    path('guardar-producto/', views.guardar_producto, name="guardar-producto"),
    path('borrar-producto/<str:nombre>', views.borrar_producto, name="borrar-producto"),
    path('carta/', views.carta, name='carta'),
]
