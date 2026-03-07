from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Baldosa(models.Model):
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    precio = models.FloatField()

    def __str__(self):
        return self.modelo


