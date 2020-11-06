from django.db import models

from django.db import models

# Create your models here.

class Libro(models.Model):
    codigo = models.CharField(max_length=3, primary_key= True)
    nombre = models.CharField(max_length=100)
    editoriales = [
        ('A', 'Ariel'),
        ('C', 'Caja Negra'),
        ('P', 'Planeta')
    ]
    editorial = models.CharField(max_length=30, choices=editoriales, default='P')
    cantidad = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre
    
    
class Boleta(models.Model):
    codigo = models.CharField(max_length=3, primary_key= True)
    editoriales = [
        ('A', 'Ariel'),
        ('C', 'Caja Negra'),
        ('P', 'Planeta')
    ]
    editorial = models.CharField(max_length=30, choices=editoriales, default='P')
    cantidad = models.IntegerField()
    vigencia = models.BooleanField(default=True)
    fecha = models.DateTimeField(auto_now_add=True)
    libro = models.ForeignKey(Libro, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo
    
    

class Editoral(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    libro = models.ForeignKey(Libro, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    id = models.IntegerField(primary_key=True)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=20)
    sucursales = [
        ('O', 'Plaza Oeste'),
        ('S', 'Plaza Sur '),
        ('A', 'Plaza Arauco')
    ]
    sucursal = models.CharField(max_length=30, choices=sucursales, default='O')

    def __str__(self):
        return self.sucursal
    