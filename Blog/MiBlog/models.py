from django.db import models
from django.contrib.auth.models import User

class autor(models.Model):
    nombre = models.CharField(max_length = 40)
    titulo = models.CharField(max_length = 40)
    post = models.TextField("")
    def __str__(self):
        return f'nombre: {self.nombre} - titulo: {self.titulo} - post: {self.post}'


class avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='images/', null=True, blank=True)
    
    
class profesor(models.Model):
    nombre = models.CharField(max_length = 40)
    deporte = models.CharField(max_length = 40)
    DNI = models.IntegerField()
    def __str__(self):
        return f'nombre: {self.nombre} - deporte: {self.deporte} - DNI: {self.DNI}'