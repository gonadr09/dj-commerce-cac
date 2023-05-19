from django.db import models
from users.models import CustomUser


class Tag(models.Model):
    nombre = models.CharField(max_length=128, verbose_name="Nombre Etiqueta")

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'

    def __str__(self):
        return self.nombre
    

class Category(models.Model):
    nombre = models.CharField(max_length=128, verbose_name="Nombre Categoría")
    padre = models.ForeignKey('self', related_name='Hijos', on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(max_length=128, unique=True, editable=False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre


class Product(models.Model):
    nombre = models.CharField(max_length=128, verbose_name="Nombre producto")
    stock = models.IntegerField(verbose_name="Cantidad en stock")
    descripcion = models.CharField(max_length=255, verbose_name="Descripción de producto")
    precio = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Precio")
    categoria = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    etiquetas = models.ManyToManyField(Tag, blank=True)
    imagen = models.ImageField(upload_to='producto/')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre


class Order(models.Model):
    PEDIDO_ESTADO = [
       ('I', 'Ingresado'),
       ('P', 'Procesando'),
       ('C', 'Cancelado'),
       ('F', 'Finalizado')
    ]
    estado = models.CharField(max_length=1, choices=PEDIDO_ESTADO, default='I')
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return self.pedido


class OrderProduct(models.Model):
    pedido = models.ForeignKey(Order, on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")

    class Meta:
        verbose_name = 'Detalle de Pedido'
        verbose_name_plural = 'Detalles de Pedido'