from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class Formulario(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    consulta = models.CharField(max_length=1000)
    direccion = models.CharField(max_length=100)
    telefonos = models.CharField(max_length=20)

"""
class Producto:
    nombreProducto = models.CharField(max_length=100)
    precioProducto = models.IntegerField()
    imagen = models.ImageField(upload_to='images', null =True, default= 'images/default.jpg')

"""