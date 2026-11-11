# models.py
from django.db import models

class Estacionamiento(models.Model):
    direccion = models.CharField(max_length=200)
    precio_por_hora = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, default='DISPONIBLE') # DISPONIBLE u OCUPADO

    def __str__(self):
        return self.direccion