from django import forms

class ProductoFormulario(forms.Form):
    nombre= forms.CharField(label="Nombre del producto")
    referencia = forms.IntegerField(label="Referencia del producto")
    precio=forms.IntegerField()
    cantidad= forms.IntegerField()


class TiendaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    codigoTienda = forms.IntegerField()
    ciudad = forms.CharField(max_length=50)
    email = forms.EmailField()

class CiudadFormulario(forms.Form):
    nombre = forms.CharField(max_length=40, label="Nombre de la tienda")
    pais = forms.CharField(max_length=40,label="País donde está la tienda")


class OfertaFormulario(forms.Form):

    nombre_oferta=  forms.CharField(max_length=40, label ="Nombre de la oferta ")
    porcentaje_oferta= forms.IntegerField(label = "Porcentaje de la oferta ")
    tienda = forms.CharField(label = "Tienda donde aplica ")

    class Meta:
        #model = OfertaFormulario
        labels = {"nombre_oferta":"Nombre de la oferta"}

   
    