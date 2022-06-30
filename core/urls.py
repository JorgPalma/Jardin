from django.urls import path
from .views import home, mispedidos, productos, publicar, misproductos, editar, borrar, comprar, pedidos, editarpedido, registro

urlpatterns = [
    path('', home, name="home"),
    path('mispedidos/', mispedidos, name="mispedidos"),
    path('productos/', productos, name="productos"),
    path('publicar/', publicar, name="publicar"),
    path('misproductos/', misproductos, name="misproductos"),
    path('editar/<id>/', editar, name="editar"),
    path('borrar/<id>/', borrar, name="borrar"),
    path('comprar/<id>/', comprar, name="comprar"),
    path('pedidos/', pedidos, name="pedidos"),
    path('editarpedido/<id>/', editarpedido, name="editarpedido"),
    path('registro/', registro, name="registro")
]
