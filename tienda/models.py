from django.db import models


class Perfume(models.Model):
    nombre = models.CharField(max_length=120)
    marca = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    ventas = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to='perfumes/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.marca}"


class Resena(models.Model):
    nombre = models.CharField(max_length=100)
    comentario = models.TextField()
    puntuacion = models.PositiveSmallIntegerField(default=5)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.puntuacion}/5)"


class Perfumeria(models.Model):
    nombre = models.CharField(max_length=120)
    ciudad = models.CharField(max_length=120, blank=True)
    ventas_totales = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-ventas_totales']

    def __str__(self):
        return self.nombre
