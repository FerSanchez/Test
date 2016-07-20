from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Libros(models.Model):
    Nombre= models.CharField(max_length=200)
    Genero= models.CharField(max_length=200, null=True)
    Descripcion= models.TextField(max_length=500, blank=True, null=True)
    Portada= models.CharField(max_length=1000, null=True)
    is_favorite= models.BooleanField(default=False)

    def __str__(self):
        return self.Nombre

class Autores(models.Model):
    Nombre= models.CharField(max_length=200)
    libros= models.ForeignKey(Libros, blank=True, null=True)
    Nacionalidad=models.CharField(max_length=100, blank=True, null=True)
    Descripcion= models.TextField(max_length=500, blank=True, null=True)
    Foto= models.CharField(max_length=1000, null=True)


    def __str__(self):
        return self.Nombre
