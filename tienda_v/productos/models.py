from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Producto(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   nom_producto = models.CharField(max_length=100,blank=True,null=True)
   precio_producto = models.FloatField(default=0)
   escala_producto = models.CharField(max_length=10, blank=True, null=True)
   tamaño = models.CharField(max_length=100,blank=True,null=True)
   imagen_Producto = models.ImageField(blank=True,null=True)

   def __str__(self) -> str:
      return self.nom_producto

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	timestamp = models.DateTimeField(default=timezone.now)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: {self.content}'
