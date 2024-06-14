from django.urls import path
from AppPreEntrega3.views import producto, tienda, oferta, ciudad, lista_productos, tiendas, ofertas, ciudades, inicio,productos


urlpatterns = [
    path('', inicio, name='Inicio'),
    path('agrega-producto/<nombre>/<referencia>/<cantidad>/<precio>/<tienda>', producto),
    path('lista-productos/', lista_productos, name='ListaProductos'),
    path('productos/', productos, name='Productos'),
    path('agrega-tienda/<nombre>/<codigoTienda>/<ciudad>/<email>', tienda),
    path('tiendas/', tiendas, name='Tiendas'),
    path('agrega-oferta/<nombre_oferta>/<tienda_donde_aplica>/<porcentaje_oferta>', oferta),
    path('ofertas/', ofertas, name='Ofertas'),
    path('agrega-ciudad/<nombre>/<pais>', ciudad),
    path('ciudades/', ciudades, name='Ciudad'),
]