from django.contrib import admin
from .models import Producto, Pedido, Estado, Comuna, Suscripcion

# Register your models here.

admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Estado)
admin.site.register(Comuna)
admin.site.register(Suscripcion)