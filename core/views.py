from gc import get_objects
import re
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForms, SuscripcionForms, CompraForms
from .models import Producto, Suscripcion, Pedido

# Create your views here.

def home(request):

    data = {
        'form': SuscripcionForms()
    }

    if request.method == 'POST':
        formulario = SuscripcionForms(data=request.POST)
        if formulario.is_valid():
            rating_form = formulario.save(commit=False)
            rating_form.usuario = request.user
            rating_form.save()
        else:
            data["form"] = formulario

    return render(request, 'core/index.html', data)

def pedidos(request):
    return render(request, 'core/pedidos.html')

def productos(request):

    productos = Producto.objects.all()
    data = {
        'productos': productos
    }

    return render(request, 'core/productos.html', data)

def publicar(request):

    data = {
        'form': ProductoForms()
    }

    if request.method == 'POST':
        formulario = ProductoForms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            rating_form = formulario.save(commit=False)
            rating_form.usuario = request.user
            rating_form.save()
        else:
            data["form"] = formulario

    return render(request, 'core/publicar.html', data)

def misproductos(request):

    productos = Producto.objects.filter(usuario = request.user)
    data = {
        'productos': productos
    }

    return render(request, 'core/misproductos.html', data)

def editar(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForms(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForms(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="misproductos")
        data["form"] = formulario
            

    return render(request, 'core/editar.html', data)

def borrar(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="misproductos")

def comprar(request, id):
    suscripcion = Suscripcion.objects.filter(usuario = request.user)

    data = {
        'producto': get_object_or_404(Producto, id=id),
        'suscripcion': suscripcion,
        'form': CompraForms()
    }

    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        formulario = CompraForms(data=request.POST)
        formulario2 = ProductoForms(data=request.POST)
        if formulario.is_valid():
            rating_form = formulario.save(commit=False)
            rating_form.usuario = request.user
            rating_form.producto = producto
            rating_form.save()
            rating_form2 = formulario2.save(commit=False)
            rating_form2.stock = producto.stock - 1
            rating_form.save()
        else:
            data["form"] = formulario

    return render(request, 'core/comprar.html', data)