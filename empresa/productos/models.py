from django.db import models

class Producto(models.Model):
    codigo = models.IntegerField(null=True)
    nombre = models.CharField(max_length=100, default='Basico')
    color = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    fecha = models.DateField()

    def __str__(self):
        return self.nombre
