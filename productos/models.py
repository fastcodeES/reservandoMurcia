from django.db import models
from django.db.models.enums import Choices

# Create your models here.

class Producto(models.Model):
    opciones = [
        ('WHISKY', 'WHISKY'),
        ('RON', 'RON'),
        ('GINEBRA', 'GINEBRA'),
        ('VODKA', 'VODKA'),
        ('SIN ALCOHOL', 'SIN ALCOHOL'),

    ]

    nombre = models.CharField(max_length=60, primary_key=True)
    descripcion = models.TextField(max_length=300)
    # imagen = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    precio = models.IntegerField(default=0)
    categoria = models.CharField(choices=opciones, max_length=20, null= True)

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.nombre