from django.db import models
from django.contrib.auth.models import User

class GuiaCombustible(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    periodo = models.CharField(max_length=50)
    fecha = models.DateField()
    nombre_conductor = models.CharField(max_length=100)
    fecha_carga = models.DateField()
    guia = models.CharField(max_length=100)
    patente = models.CharField(max_length=20)
    estacion_servicio = models.CharField(max_length=100)
    suministro = models.DecimalField(max_digits=10, decimal_places=2)
    kms = models.IntegerField()
    consumo = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='imagenes_guias/')

    def __str__(self):
        return self.titulo
