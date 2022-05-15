from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic.edit import DeleteView
# Create your views here.

def contacto(request):
    data = {
        'form': ContactoForm()
    } 
    if request.method == "POST":
        formulario = ContactoForm(data= request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje enviado"
        else:
            data["form"] = formulario

    return render(request, 'contactos.html', data)

def borrar_mensaje(request, id):
    mensaje = Contacto.objects.get(pk=id)

    mensaje.delete()

    return redirect('mensajes')

def mensajes(request):
    contactos = Contacto.objects.all()

    return render(request, 'mensajes.html', {'contactos': contactos})

def respuestas(request, email):
    data = {
        'form': RespuestasForm()
    } 
    if request.method == "POST":

        subjet = request.POST["asunto"]
        message=request.POST["mensaje"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list=email
        list_email = [recipient_list]

        send_mail(subjet, message, email_from, list_email)

    return render(request, 'respuestas.html', data)
