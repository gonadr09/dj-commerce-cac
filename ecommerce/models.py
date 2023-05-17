from django.db import models


# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=128, verbose_name="Nombre Usuario")
    apellido = models.CharField(max_length=128, verbose_name="Apellido")
    mail = models.EmailField(verbose_name="Mail")
    dni = models.CharField(max_length=8, verbose_name="DNI", null=True)


class Producto(models.Model):
    nombre = models.CharField(max_length=128, verbose_name="Nombre Producto")
    stock = models.IntegerField(verbose_name="Cantidad en Stock")
    descripcion = models.CharField(verbose_name="Descripción de Producto")
    precio = models.IntegerField(verbose_name="Precio")


class Categoria(models.Model):
    nombre = models.CharField(max_length=128, verbose_name="Nombre Categoría")
    productos = models.ManyToManyField(Producto)


class Compra(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name="Cantiadad Comprada")
