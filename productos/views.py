from django.shortcuts import redirect, render
from .models import * 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

def carta(request):

    if request.method == 'POST':

        tipo = request.POST['categoria']

        if tipo == 'TODOS' or tipo == 'None':

            producto = Producto.objects.all()

            return render(request, 'carta.html', {'productos': producto, 'categoria': tipo})

        
        else:

            producto = Producto.objects.all().filter(categoria=tipo)

            return render(request, 'carta.html', {'productos': producto, 'categoria': tipo})

    else:

        producto = Producto.objects.all()

        tipo = "Todos"

        return render(request, 'carta.html', {'productos': producto, 'categoria': tipo})

@staff_member_required 
def crear_producto(request):

    return render(request, 'crear_producto.html')

@staff_member_required
def guardar_producto(request):

    if request.method == 'POST':
        nombre = request.POST['nombre']
        # validaciones
        if nombre == '':
            data = "Debes introducir el nombre de un producto"
            return render(request, "crear_producto.html", {'data' : data})

        descripcion = request.POST['descripcion']
        precio = request.POST['precio']

        if precio == '':

            precio = '0'

            precio = int(precio)

        
        categoria = request.POST['categoria']
        producto = Producto(
            nombre = nombre,
            descripcion = descripcion,
            precio = precio,
            categoria = categoria
        )
        producto.save()

        return redirect('carta')
   
    else:
        return HttpResponse("No se ha podido crear")

    # return render(request, 'crear_producto.html')

@staff_member_required
def borrar_producto(request, nombre):

    producto = Producto.objects.get(pk=nombre)

    producto.delete()

    return redirect('carta')