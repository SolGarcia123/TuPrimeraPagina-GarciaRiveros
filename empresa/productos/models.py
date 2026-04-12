from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

imagen = models.ImageField(upload_to='productos', null=True, blank=True)