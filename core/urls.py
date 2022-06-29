from django.urls import path
from .views import home, pedidos, productos, publicar, misproductos, editar, borrar, comprar

urlpatterns = [
    path('', home, name="home"),
    path('pedidos/', pedidos, name="pedidos"),
    path('productos/', productos, name="productos"),
    path('publicar/', publicar, name="publicar"),
    path('misproductos/', misproductos, name="misproductos"),
    path('editar/<id>/', editar, name="editar"),
    path('borrar/<id>/', borrar, name="borrar"),
    path('comprar/<id>/', comprar, name="comprar")
]
