from django import forms
from .models import Producto, Suscripcion, Pedido

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