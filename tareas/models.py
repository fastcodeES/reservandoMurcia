from django.db import models

# Create your models here.


class Tarea (models.Model):


    completed = [
    [0, "SI"],
    [1, "NO"],   
]

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    # completado = models.IntegerField(choices=completed)
    
    def __str__(self):
        return self.titulo

