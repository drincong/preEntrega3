from django.db import models

# Create your models here.

class Tienda(models.Model):
    nombre = models.CharField(max_length=40)
    codigoTienda = models.IntegerField()
    ciudad = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} - {self.codigoTienda}'
    
    class Meta():
        ordering=('nombre','codigoTienda')
        unique_together = ('nombre','codigoTienda')

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    referencia = models.IntegerField()
    cantidad = models.IntegerField() 
    precio = models.IntegerField()

    class Meta():
        ordering=('nombre','referencia')
        unique_together = ('nombre','referencia')

    
    def __str__(self):
        return f'{self.nombre} - {self.referencia}'

class Oferta(models.Model):
    nombre_oferta=  models.CharField(max_length=40)
    porcentaje_oferta= models.IntegerField()
    tienda = models.ManyToManyField(Tienda)

    class Meta():
        ordering=('nombre_oferta','porcentaje_oferta')
        unique_together = ('nombre_oferta','porcentaje_oferta')

    def __str__(self):
        return f'{self.nombre_oferta} - {self.porcentaje_oferta}%'

class Ciudad(models.Model):
    nombre= models.CharField(max_length=40)
    pais = models.CharField(max_length=30)

    class Meta():
        verbose_name_plural='Ciudades'
        unique_together = ('nombre', 'pais')
    

    def __str__(self):
        return f'{self.nombre} - {self.pais}'

