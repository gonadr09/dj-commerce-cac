from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class CustomUser(AbstractUser):
    dni = models.IntegerField(max_length=15, verbose_name="DNI")
    phone = models.CharField(max_length=50, verbose_name="Teléfono")
    address = models.CharField(max_length=100, verbose_name="Dirección")
    city = models.ForeignKey(max_length=50, verbose_name="Ciudad")
    state = models.ForeignKey(max_length=50, verbose_name="Provincia")

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.username