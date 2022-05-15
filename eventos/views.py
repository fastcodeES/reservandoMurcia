from django.shortcuts import redirect, render
from .models import *
from django.views import generic
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

from django.http import HttpResponse


def index(request):

    evento = Evento.objects.all()

    return render(request, 'home.html', {'eventos': evento})


class ver_evento(generic.DetailView):
    model = Evento
    template_name = "eventos/ver-evento.html"

@staff_member_required
def eliminar_eventos(request, id):

    evento = Evento.objects.get(pk=id)

    evento.delete()

    return redirect('index')

@staff_member_required
def crear_evento(request):

    return render(request, 'eventos/crear-evento.html')

@staff_member_required
def guardar_evento(request):

    if request.method == 'POST':

        titulo = request.POST['titulo']
        # validaciones

        if titulo == '':
            data = "Debes introducir el título del evento"
            return render(request, "eventos/crear-evento.html", {'data' : data})
        try:
            imagen = request.FILES['imagen']
        except:
            imagen = ""         

        descripcion = request.POST['descripcion']

        evento = Evento(
            titulo=titulo,
            descripcion=descripcion,
            imagen=imagen,
        )

        evento.save()

        return redirect('index')

    else:
        return HttpResponse("No se ha podido crear")


