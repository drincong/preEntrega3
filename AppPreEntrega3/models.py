from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    referencia = models.IntegerField()
    cantidad = models.IntegerField() 
    precio = models.IntegerField()
    tienda = models.IntegerField()

class Tienda(models.Model):
    nombre = models.CharField(max_length=40)
    codigoTienda = models.IntegerField()
    ciudad = models.CharField(max_length=50)
    email = models.EmailField()

class Oferta(models.Model):
    nombre_oferta=  models.CharField(max_length=40)
    tienda_donde_aplica= models.CharField(max_length=50)
    porcentaje_oferta= models.IntegerField()

class Ciudad(models.Model):
    nombre= models.CharField(max_length=40)
    pais = models.CharField(max_length=30)



