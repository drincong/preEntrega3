from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto, Tienda, Oferta, Ciudad

def producto (req, nombre,referencia,cantidad,precio,tienda):
    nuevo_producto = Producto(nombre = nombre, referencia = referencia, cantidad= cantidad, precio = precio, tienda=tienda)
    nuevo_producto.save()

    return  HttpResponse (f"""
    <p>  Producto {nuevo_producto.nombre} con referencia {nuevo_producto.referencia}  creado con exito </p>
    """)

def tienda (req, nombre,codigoTienda,ciudad, email ):
    nueva_tienda = Tienda(nombre = nombre,codigoTienda = codigoTienda, ciudad=ciudad, email = email)
    nueva_tienda.save()

    return  HttpResponse (f"""
    <p>  Tienda {nueva_tienda.nombre} con código {nueva_tienda.codigoTienda}  creada con éxito </p>
    """)

def oferta (req, nombre_oferta, tienda_donde_aplica,porcentaje_oferta):
    nueva_oferta = Oferta(nombre_oferta = nombre_oferta, tienda_donde_aplica = tienda_donde_aplica, porcentaje_oferta = porcentaje_oferta)
    nueva_oferta.save()

    return  HttpResponse (f"""
    <p>  Oferta {nueva_oferta.nombre_oferta} con el {nueva_oferta.porcentaje_oferta} % de descuento para la tienda {nueva_oferta.tienda} creada con éxito </p>
    """)

def ciudad (req, nombre, pais):
    nueva_ciudad = Ciudad(nombre = nombre, pais = pais)
    nueva_ciudad.save()

    return  HttpResponse (f"""
    <p>  La ciudad de {nueva_ciudad.nombre} ubicada en el país: {nueva_ciudad.pais} ha sido creada con éxito </p>
    """)

def lista_productos (req):
    lista = Producto.objects.all()

    return render(req, "lista_productos.html", {"lista_productos" : lista})

def productos (req):
    lista = Producto.objects.all()

    return render(req, "productos.html", {"productos" : lista})


def tiendas (req):
    lista = Tienda.objects.all()

    return render(req, "tiendas.html", {"tiendas" : lista})


def ofertas (req):
    lista = Oferta.objects.all()

    return render(req, "ofertas.html", {"ofertas" : lista})

def ciudades (req):
    lista = Ciudad.objects.all()

    return render(req, "ciudades.html", {"ciudades" : lista})

def inicio(req):
    
     return render(req, "inicio.html", {})
