from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    dni = models.CharField(max_length=15, verbose_name="DNI", null=True, blank=True)
    phone = models.CharField(max_length=50, verbose_name="Teléfono", null=True, blank=True)
    address = models.CharField(max_length=100, verbose_name="Dirección", null=True, blank=True)
    city = models.CharField(max_length=50, verbose_name="Ciudad", null=True, blank=True)
    state = models.CharField(max_length=50, verbose_name="Provincia", null=True, blank=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.username
