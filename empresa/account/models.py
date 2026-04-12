from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    dni = models.IntegerField()
    imagen = models.ImageField(upload_to='perfiles/', null=True, blank=True)

    def __str__(self):
        return self.user.username