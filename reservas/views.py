from django.contrib.postgres import fields
from django.db.models.base import Model
from django.shortcuts import redirect, render
from .models import *
from django.views import generic
from django.contrib import messages
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from time import gmtime, strftime
from django.views.generic import TemplateView, CreateView
from django.core.paginator import Paginator


@login_required(login_url='login')
def crear_reserva(request):
    data = {
        'form': ReservasForm()
    }
    if request.method == "POST":
        formulario = ReservasForm(data=request.POST)
        if formulario.is_valid():

            # Valida que las reservas dependan de las mesas disponibles
            horario = formulario['horario'].data
            n_mesas = Mesa.objects.all().count()
            validacion_personal = True
            fecha = formulario['fecha_reserva'].data
            partes = fecha.split("/")
            fecha_reversed = ("-").join(reversed(partes))
            fechas_coincidentes = Reserva.objects.all().filter(
                fecha_reserva=fecha_reversed, horario=horario).count()
            # Valida que la misma persona no haga mas de 2 reservas el mismo dia
            usuario = request.user.username
            usuario_coincidente = Reserva.objects.all().filter(
                username=usuario, fecha_reserva=fecha_reversed).count()

            razon = 0
            if fechas_coincidentes >= n_mesas:
                validacion_personal = False
                razon = 1
            if usuario_coincidente > 0:
                validacion_personal = False
                razon = 2

            if validacion_personal:
                f = Reserva(
                    nombre=formulario['nombre'].data,
                    email=formulario['email'].data,
                    numero_asistentes=formulario['numero_asistentes'].data,
                    fecha_reserva=fecha_reversed,
                    username=request.user.username,
                    telefono=formulario['telefono'].data,
                    horario=formulario['horario'].data
                )
                f.save()
                data["mensaje"] = "Reserva aceptada"
            else:
                if razon == 1:
                    data["error"] = "Reserva denegada, hoy no quedan reservas para esta hora"
                else:
                    data["error"] = "Reserva denegada, un mismo usuario no puede reservar más de dos mesas el mismo día"

        else:
            data["form"] = formulario

    return render(request, 'reservas/crear-reservas.html', data)

@login_required(login_url='login')
def mis_reservas(request):
    usuario = request.user.username
    usuario_coincidente = Reserva.objects.all().filter(username=usuario).order_by('-fecha_reserva')
    numero = Reserva.objects.all().filter(username=usuario).count()
    if request.method == "POST":
        fecha =  request.POST['fecha']
        if fecha == '':
            usuario_coincidente = Reserva.objects.all().filter(username=usuario).order_by('-fecha_reserva')
            numero = Reserva.objects.all().filter(username=usuario).count()
            return render(request, 'reservas/mis-reservas.html', {'usuarios': usuario_coincidente, 'numero':numero})
        
        partes = fecha.split("/")
        fecha_reversed = ("-").join(reversed(partes))
        usuario_coincidente = Reserva.objects.all().filter(fecha_reserva=fecha_reversed, username=usuario)
        numero = Reserva.objects.all().filter(fecha_reserva=fecha_reversed, username=usuario).count()
        return render(request, 'reservas/mis-reservas.html', {'usuarios': usuario_coincidente, 'numero':numero})
    return render(request, 'reservas/mis-reservas.html', {'usuarios': usuario_coincidente, 'numero':numero})


def reservas(request):
    
    if request.method == "POST":
        fecha =  request.POST['fecha']
        if fecha == '':
            reservas = Reserva.objects.all()
            numero = Reserva.objects.all().count()
            return render(request, 'reservas/reservas.html', {'reservas': reservas, 'numero':numero})

        partes = fecha.split("/")
        fecha_reversed = ("-").join(reversed(partes))
        reservas = Reserva.objects.all().filter(fecha_reserva=fecha_reversed)
        numero = Reserva.objects.all().filter(fecha_reserva=fecha_reversed).count()
        return render(request, 'reservas/reservas.html', {'reservas': reservas, 'numero':numero})
    else:
        reservas = Reserva.objects.all()
        numero = Reserva.objects.all().count()

        return render(request, 'reservas/reservas.html', {'reservas': reservas, 'numero':numero})


def borrar_reserva(request, id):

    reserva = Reserva.objects.get(pk=id)

    reserva.delete()

    return redirect('todas-reservas')



class error404(TemplateView):

    template_name = "error404.html"

def crear_mesa(request):

    data = {
        'mesa': Mesa.objects.all()
    }

    if request.method == "POST":
        nombre = request.POST['nombre']
        mesa = Mesa(
            nombre = nombre,
        )

        mesa.save()
    
    return render(request, 'reservas/crear-mesas.html', data)

def eliminar_mesa(request, id):

    mesa = Mesa.objects.all().get(id = id)

    mesa.delete()
    
    return redirect('crear-mesa')