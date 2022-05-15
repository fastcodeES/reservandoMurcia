from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Evento(models.Model):

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=True)
    descripcion = models.TextField(max_length=1000, null = True)

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.titulo

    def __unicode__(self,):

        return str(self.imagen)