from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.TextField(max_length=60)
    descripcion_producto = models.TextField(max_length=255)
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre_producto
    
class Usuarios(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre_usuario = models.TextField(max_length=60)
    password = models.TextField(max_length=255)

    def __str__(self):
        return self.nombre_usuario