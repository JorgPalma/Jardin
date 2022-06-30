from gc import get_objects
import re
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForms, SuscripcionForms, CompraForms, PedidoForms, CustomUserCreationForm
from .models import Producto, Suscripcion, Pedido
from django.contrib.auth import authenticate, login

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

def mispedidos(request):

    data = {
        'pedidos': Pedido.objects.filter(usuario = request.user)
    }

    return render(request, 'core/mispedidos.html', data)

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
    producto = get_object_or_404(Producto, id=id)

    data = {
        'producto': get_object_or_404(Producto, id=id),
        'suscripcion': suscripcion,
        'form': CompraForms(),
    }


    if request.method == 'POST':
        formulario = CompraForms(data=request.POST)
        if formulario.is_valid():
            rating_form = formulario.save(commit=False)
            rating_form.usuario = request.user
            rating_form.producto = producto
            rating_form.save()
        else:
            data["form"] = formulario

    return render(request, 'core/comprar.html', data)

def pedidos(request):

    data = {
        'pedidos': Pedido.objects.all(),
    }

    return render(request, 'core/pedidos.html', data)

def editarpedido(request, id):

    pedido = get_object_or_404(Pedido, id=id)

    data = {
        'form': PedidoForms(instance=pedido)
    }

    if request.method == 'POST':
        formulario = PedidoForms(data=request.POST, instance=pedido, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="pedidos")
        data["form"] = formulario
            

    return render(request, 'core/editarpedido.html', data)

def registro(request):

    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="home")
        else:
            data["form"] = formulario

    return render(request, 'registration/registro.html', data)