from django.db import models

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.CharField(max_length=255)
    autor = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
