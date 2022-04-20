from mailbox import NoSuchMailboxError
from django.db import models

# Create your models here.
class grado(models.Model):
    nombre = models.CharField(max_length=50)
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.nombre)

class seccion(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.nombre)

class establecimiento(models.Model):
    nombre = models.CharField(max_length=50) 
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField(max_length=15)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return '%s' % (self.nombre)

class imagenes(models.Model):
    nombre = models.CharField(max_length=50)
    archivo = models.FileField(upload_to="archivos/", null=True, blank=True)
    creditos = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.nombre)

class videos(models.Model):
    nombre = models.CharField(max_length=50)
    link = models.CharField(max_length=500)
    creditos = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.nombre)

class ejemplos(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=500)

    def __str__(self):
        return '%s' % (self.titulo)

class area(models.Model):
    nombre = models.CharField(max_length=50)
    info = models.CharField(max_length=500)

    def __str__(self):
        return '%s' % (self.nombre)

class tema(models.Model):
    nombre = models.CharField(max_length=50)
    info = models.CharField(max_length=500)
    IDarea=models.ForeignKey(
        'area',
        on_delete=models.CASCADE,
        default=1
        )

    def __str__(self):
        return '%s' % (self.nombre)

class pregunta(models.Model):
    pregunta = models.CharField(max_length=50)
    IDtema=models.ForeignKey(
        'tema',
        on_delete=models.CASCADE,
        default=1
        )
    IDrespuesta=models.ForeignKey(
        'respuesta',
        on_delete=models.CASCADE,
        default=1
        )

    def __str__(self):
        return '%s' % (self.pregunta)

class respuesta(models.Model):
    respuesta = models.CharField(max_length=50)
    IDtema=models.ForeignKey(
        'tema',
        on_delete=models.CASCADE,
        default=1
        )

    def __str__(self):
        return '%s' % (self.respuesta)