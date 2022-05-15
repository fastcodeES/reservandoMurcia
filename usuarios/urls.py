from django.urls import path
from usuarios import views


urlpatterns = [
    path('usuarios/', views.listar_usuarios, name="listar-usuarios"),
    path('modificar-usuario/<int:pk>', views.UserUpdateView.as_view(), name="modificar-usuario"),
    path('eliminar-usuario/<int:pk>', views.eliminar_usuario, name="eliminar-usuario"),
]
