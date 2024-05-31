from django.db import models

# Create your models here.
'''
class usuario(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    usuario = models.CharField(max_length=100,blank=True, null=True)
    contraseña = models.CharField(max_length=100, blank=True, null=True)
    edad = models.IntegerField(default=0)
    registro = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nombre'''

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    usuario = models.CharField(max_length=100,blank=True, null=True)
    contraseña = models.CharField(max_length=100, blank=True, null=True)
    edad = models.IntegerField(default=0)
    registro = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
      return self.nombre

