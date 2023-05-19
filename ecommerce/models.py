from django.db import models
from users.models import CustomUser


class Categoria(models.Model):
    nombre = models.CharField(max_length=128, verbose_name="Nombre Categoría")


class Producto(models.Model):
    nombre = models.CharField(max_length=128, verbose_name="Nombre Producto")
    stock = models.IntegerField(verbose_name="Cantidad en Stock")
    descripcion = models.CharField(verbose_name="Descripción de Producto")
    precio = models.IntegerField(verbose_name="Precio")
    categoria = models.ForeignKey(Categoria)
    imagen = models.ImageField()


class Compra(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name="Cantiadad Comprada")
