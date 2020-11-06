from django.contrib import admin
from .models import Libro
from .models import Editoral
from .models import Sucursal
from .models import Boleta

# Register your models here.

class LibroAdmin(admin.ModelAdmin):
    list_display    = ['codigo','nombre','cantidad','editorial','precio']

admin.site.register(Libro, LibroAdmin)

class EditorialAdmin(admin.ModelAdmin):
    list_display    = ['codigo','nombre', 'cantidad', 'libro']

admin.site.register(Editoral, EditorialAdmin)

class SucursalAdmin(admin.ModelAdmin):
    list_display    = ['id','telefono','direccion','sucursal']

admin.site.register(Sucursal, SucursalAdmin)

class BoletaAdmin(admin.ModelAdmin):
    list_display    = ['editorial','cantidad','vigencia','codigo', 'fecha']

admin.site.register(Boleta, BoletaAdmin)
