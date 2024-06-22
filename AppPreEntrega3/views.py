from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto, Tienda, Oferta, Ciudad
from .forms import ProductoFormulario, TiendaFormulario, CiudadFormulario, OfertaFormulario

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

def producto_formulario(req):

    # print('method: ',req.method)
    # print('POST: ',req.POST)

    if req.method == 'POST':

        miformulario = ProductoFormulario(req.POST)

        #print(miformulario)

        if miformulario.is_valid():

            data = miformulario.cleaned_data

            nuevo_producto = Producto(nombre = data['nombre'], referencia = data['referencia'], cantidad= data['cantidad'], precio = data['precio'])
            nuevo_producto.save()
            
            return render(req,"inicio.html",{"message": "Curso creado con éxito"})
        else:
            return render(req,"inicio.html",{"message": "Datos inválidos"})
    else:

        miformulario = ProductoFormulario()
        return render(req,"producto_formulario.html",{"miformulario": miformulario})



def tienda_formulario(req):
    if req.method == 'POST':

        miformulario = TiendaFormulario(req.POST)

        #print(miformulario)

        if miformulario.is_valid():

            data = miformulario.cleaned_data

            nueva_tienda = Tienda(nombre = data['nombre'], codigoTienda = data['codigoTienda'], ciudad= data['ciudad'], email = data['email'])
            nueva_tienda.save()
            
            return render(req,"inicio.html",{"message": "Tienda creada con éxito"})
        else:
            return render(req,"inicio.html",{"message": "Datos inválidos"})
    else:

        miformulario = TiendaFormulario()
        return render(req,"tienda_formulario.html",{"miformulario": miformulario})
    


def ciudad_formulario(req):
    if req.method == 'POST':

        miformulario = CiudadFormulario(req.POST)

        #print(miformulario)

        if miformulario.is_valid():

            data = miformulario.cleaned_data

            nueva_ciudad = Ciudad(nombre = data['nombre'], pais = data['pais'])
            nueva_ciudad.save()
            
            return render(req,"inicio.html",{"message": "Ciudad creada con éxito"})
        else:
            return render(req,"inicio.html",{"message": "Datos inválidos"})
    else:
        miformulario = CiudadFormulario()
        return render(req,"ciudad_formulario.html",{"miformulario": miformulario})
    


def oferta_formulario(req):
    if req.method == 'POST':

        miformulario = OfertaFormulario(req.POST)

        #print(miformulario)

        if miformulario.is_valid():

            data = miformulario.cleaned_data

            nueva_oferta = Oferta(nombre_oferta = data['nombre_oferta'], porcentaje_oferta = data['porcentaje_oferta'], tienda = data['tienda'])
            nueva_oferta.save()
            
            return render(req,"inicio.html",{"message": "Oferta creada con éxito"})
        else:
            return render(req,"inicio.html",{"message": "Datos inválidos"})
    else:
        miformulario = OfertaFormulario()
        return render(req,"oferta_formulario.html",{"miformulario": miformulario})
    

def busqueda_referencia(req):
    return render(req,"buscar_referencia.html",{})


def buscar(req):
    #return HttpResponse (f'Estoy buscando la referencia {req.GET["referencia"]}')
    if req.GET["referencia"]:

        referencia = req.GET["referencia"]

        #producto = Producto.objects.get(referencia = referencia)
        productosEncontrados = Producto.objects.filter(referencia__icontains = referencia)

        return render(req,"resultadoBusqueda.html",{"productosEncontrados": productosEncontrados, "referencia":referencia})
    else:
            return render(req,"inicio.html",{"message": "Referencia no existente"})
   



    