from django import forms
from .models import Producto, Suscripcion, Pedido
from django.contrib.auth.forms import UserCreationForm

class ProductoForms(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'stock', 'precio', 'imagen']

class SuscripcionForms(forms.ModelForm):

    class Meta:
        model = Suscripcion
        fields = ['suscrito']

class CompraForms(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = ['comuna', 'direccion']

class PedidoForms(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = ['estado']

class CustomUserCreationForm(UserCreationForm):
    pass