from django.db import models
from users.models import CustomUser
from django.utils.text import slugify
from django.core.exceptions import ValidationError


class Tag(models.Model):
    name = models.CharField(max_length=128, verbose_name="Etiqueta")
    slug = models.SlugField(max_length=128, unique=True)

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'

    def __str__(self):
        return self.name   


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name="Categoría", unique=True)
    padre = models.ForeignKey('self', related_name='Children', on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(max_length=128, unique=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name

    def get_ancestors(self):
        ancestors = []
        category = self
        while category.padre:
            ancestors.append(category.padre)
            category = category.padre
        return ancestors

class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name="Nombre de producto")
    description = models.CharField(max_length=255, verbose_name="Descripción de producto")
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Precio")
    on_sale = models.BooleanField(default=False, verbose_name="Oferta")
    stock = models.IntegerField(verbose_name="Cantidad en stock")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Categoría")
    tag = models.ManyToManyField(Tag, blank=True, verbose_name="Etiqueta")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name
    
    def get_main_image(self):
        return self.image_set.first()

    def get_images(self):
        return self.image_set.all()
    

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='producto/', verbose_name="Imagen")

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'

    def __str__(self):
        return self.image.name


class Order(models.Model):
    STATUS_ORDER = [
       ('I', 'Ingresado'),
       ('P', 'Procesando'),
       ('C', 'Cancelado'),
       ('F', 'Finalizado')
    ]
    status = models.CharField(max_length=1, choices=STATUS_ORDER, default='I')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product, through='OrderProduct')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return self.id


class OrderProduct(models.Model):
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    pedido = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Producto del pedido'
        verbose_name_plural = 'Productos del Pedido'

    def __str__(self):
        return self.producto