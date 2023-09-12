from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Autor(models.Model):
    nombre = models.CharField("Nombre",max_length=256 )
    nacionalidad = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField ("Nombre de la categoría", max_length=48 , unique=True,)
    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField('Nombre', max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    año = models.IntegerField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    descripcion = models.TextField()
    img = models.ImageField(upload_to='libros_img')
    def __str__(self):
        return self.titulo


class Prestamo(models.Model):
    libro = models.ForeignKey (Libro , on_delete=models.CASCADE)
    usuario = models.ForeignKey(User , on_delete=models.CASCADE)
    retiro = models.DateTimeField()
    reintegro = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.reintegro:
            self.reintegro = self.retiro + timedelta(days=7)
        super().save(*args, **kwargs)
