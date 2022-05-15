from django.db import models
# Create your models here.
opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [3, "sugerencia"]
]

class Contacto(models.Model):
    id = models.AutoField(primary_key=True)    
    nombre = models.CharField(max_length=50)
    correo = models.EmailField( max_length=254)
    tipo_consultas = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField(max_length=3000)
    fecha_mensaje= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    

class Respuestas(models.Model):
    asunto = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    mensaje = models.TextField(max_length=300)

    def __str__(self):
        return self.nombre
    