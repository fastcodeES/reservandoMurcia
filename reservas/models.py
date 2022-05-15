from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.


asistentes = [
    [1, "1"],
    [2, "2"],
    [3, "3"],
    [4, "4"],
]

horario = [
    [15, "15:00"],
    [19, "19:00"],
]

class Reserva(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    numero_asistentes = models.IntegerField(choices=asistentes)
    fecha_reserva = models.DateField(auto_now=False, auto_now_add=False)
    username = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    fecha= models.DateTimeField(auto_now=True)
    horario = models.IntegerField(choices=horario)

    def __str__(self):
            return self.username + " " + "| " + str(self.fecha_reserva) + " |" 

class Mesa(models.Model):
    id = models.AutoField(primary_key=True, unique=True) 
    nombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
            return self.nombre 
    