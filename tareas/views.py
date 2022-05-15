from django.shortcuts import render, redirect
from .forms import *
from .models import *
# Create your views here.

def tareas(request):
    
    data = {
        'form': TareasForm(),
        'tareas': Tarea.objects.all(),
        'n_tareas': Tarea.objects.all().count()

    }

    if request.method == 'POST':

        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']

        tarea = Tarea(
            titulo = titulo,
            descripcion = descripcion,
        )

        tarea.save()


    return render(request, 'tareas.html', data)

def eliminar_tarea(request, id):

    tarea = Tarea.objects.get(pk=id) 

    tarea.delete()

    return redirect('tareas')

        