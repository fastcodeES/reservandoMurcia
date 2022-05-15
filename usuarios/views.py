from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.generic.edit import UpdateView

@login_required(login_url='login')
def listar_usuarios(request):
    usuarios = User.objects.all()
    n_usuarios = User.objects.all().count()

    return render(request, 'usuarios.html', {'users':usuarios, 'n_usuarios': n_usuarios})


class UserUpdateView(UpdateView):
    model = User
    template_name = "userUpdate.html"
    fields=['first_name','last_name', 'email', 'last_login', 'date_joined', 'is_staff']
    # exclude=['password', ]
    success_url ="/"



def eliminar_usuario(request, pk):

    usuario = User.objects.get(id=pk)

    usuario.delete()

    return redirect('index')