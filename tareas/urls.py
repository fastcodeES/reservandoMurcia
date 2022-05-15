from django.urls import path
from . import views

urlpatterns = [

    path('tareas/', views.tareas, name="tareas"),
    path('eliminar-tarea/<int:id>', views.eliminar_tarea, name="eliminar_tarea"),

]
