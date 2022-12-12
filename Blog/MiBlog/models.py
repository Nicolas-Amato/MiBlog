from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User

class autor(models.Model):
    nombre = models.CharField(max_length = 40)
    titulo = models.CharField(max_length = 40)
    email = models.EmailField()
    fecha = models.DateField(auto_now_add=True)
    subtitulo = models.CharField(max_length=100)
    post = models.TextField("")
    def __str__(self):
        return f' {self.nombre} {self.titulo}'


class avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='images/', null=True, blank=True)
    
    
