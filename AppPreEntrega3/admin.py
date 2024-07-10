from django.contrib import admin
from .models import Producto, Tienda, Ciudad, Oferta


class prodAdmin(admin.ModelAdmin):
    list_display = ['nombre','referencia']
    search_fields = ['nombre']
    list_filter = ['nombre']


class tiendaAdmin(admin.ModelAdmin):
    list_display = ['nombre','codigoTienda','ciudad','email']
    search_fields = ['nombre']
    list_filter = ['nombre']

class ciudadAdmin(admin.ModelAdmin):
    list_display = ['nombre','pais']
    search_fields = ['nombre']
    list_filter = ['nombre']

class ofertaAdmin(admin.ModelAdmin):
    id = ["id",]
    list_display = ['nombre_oferta','porcentaje_oferta']
    search_fields = ['nombre_oferta']
    list_filter = ['nombre_oferta']

# Register your models here.
admin.site.register(Producto, prodAdmin)
admin.site.register(Tienda,tiendaAdmin)
admin.site.register(Ciudad,ciudadAdmin)
admin.site.register(Oferta, ofertaAdmin)