"""
URL configuration for preEntrega_3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppPreEntrega3.views import producto, tienda, oferta, ciudad, lista_productos, lista_tiendas, lista_ofertas, lista_ciudades


urlpatterns = [
    path('admin/', admin.site.urls),
    path('agrega-producto/<nombre>/<referencia>/<cantidad>/<precio>/<tienda>', producto),
    path('lista-productos/', lista_productos),
    path('agrega-tienda/<nombre>/<codigoTienda>/<ciudad>/<email>', tienda),
    path('lista-tiendas/', lista_tiendas),
    path('agrega-oferta/<nombre_oferta>/<tienda_donde_aplica>/<porcentaje_oferta>', oferta),
    path('lista-ofertas/', lista_ofertas),
    path('agrega-ciudad/<nombre>/<pais>', ciudad),
    path('lista-ciudades/', lista_ciudades),

]
