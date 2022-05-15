from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def Perfil(request):
   
    return render(request, 'perfil.html')

def cambiar_contrasenia(request):
    data = {
        'form': ChangePasswordForm(),
        'fEmail': ChangeEmailForm(),

    }

    if request.method == "POST":
        usuario = request.user.username
        u = User.objects.get(username__exact = usuario )
        password = ""
        
        try:
            password = request.POST["password"]
            password1 = request.POST["password1"]
        except:
            print("An exception occurred")


        if  len(password)>0:
            contrasenia = request.POST["password"]
            if len(contrasenia )< 8:
                return render(request, 'perfil.html', { 'error': "La contraseña es demasiado corta", 'form' : ChangePasswordForm() })
            if password != password1:
                return render(request, 'perfil.html', { 'error': "Las contraseñas deben coincidir", 'form' : ChangePasswordForm() })
            u.set_password(contrasenia)
            u.save()
            return render(request, 'perfil.html', { 'mensaje': "Contraseña cambiada con exito", 'form' : ChangePasswordForm() })
    
    return render(request, 'contrasenia.html', data)
    
class UserUpdatePerfil(UpdateView):
    model = User
    template_name = "modificar-perfil.html"
    fields=['first_name', 'last_name', 'email']
    success_url ="/"