from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Comuna(models.Model):
    comuna = models.CharField(default="Comuna", max_length=20)

    def __str__(self):
        return self.comuna

class Estado(models.Model):
    estado = models.CharField(max_length=20)

    def __str__(self):
        return self.estado

class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    stock = models.IntegerField()
    precio = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='usuario')
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre

class Suscripcion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='usuarioSub')
    suscrito = models.BooleanField()

    def __str__(self):
        return self.usuario

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='usuarioVenta')
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT,null=True, blank=True)
    fecha = models.DateTimeField(default=timezone.now)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    direccion = models.CharField(max_length=50)
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)

    def __str__(self):
        return self.direccion