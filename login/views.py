from django.shortcuts import redirect, render
from .models import * 
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from .forms import registro_usuarios
from django.contrib import messages

# Create your views here.

def registro(request):

    if request.method == 'POST':
        form = registro_usuarios(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} ha sido creado')
            return redirect('login')

    else:
        form = registro_usuarios()
    
    context = {'form' : form}
    return render(request, 'registro.html', context)

        
def login(request):

    return render(request, 'login.html')