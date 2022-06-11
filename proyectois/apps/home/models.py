from pyexpat import model
from tkinter import CASCADE
from turtle import ondrag
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, nombres, apellidos,password = None):
        if not email:
            raise ValueError('El usuario debe tener un correo')
        usuario = self.model(
        username = username, 
        email = self.normalize_email(email), 
        nombres= nombres,
        apellidos = apellidos)

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, email, nombres, apellidos, password):
        usuario = self.create_user(
        email,
        username = username, 
        nombres= nombres,
        apellidos = apellidos,
        password=password
        )
        usuario.usuario_administrador = True
        
        usuario.save()
        return usuario


class UsuarioAlumnos(AbstractBaseUser):
    username = models.CharField('Nombre de Usuario', unique = True,max_length=50)
    email= models.EmailField('Correo Electronico', max_length=254, unique= True)    
    nombres = models.CharField('Nombres', max_length=250)
    apellidos = models.CharField('Apellidos', max_length=250)

    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=True)

    objects = UsuarioManager()
  
    IDSeccion = models.ForeignKey(
        'Seccion',
        on_delete=models.CASCADE,
        default=1)

    IDGrado = models.ForeignKey(
        'Grado',
        on_delete=models.CASCADE,
        default=1)
        
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS= ['email','password','nombres','apellidos']

    def __str__(self):
        return f'{self.nombres},{self.apellidos}'

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador

class Seccion(models.Model):
    nombre = models.CharField('Nombre',max_length=50, unique=True)
    def __str__(self):
        return '%s' % (self.nombre)

class Grado(models.Model):
    nombre = models.CharField('Nombre', max_length=50, unique=True)

    def __str__(self):
        return '%s' % (self.nombre)

class Estadisticas(models.Model):
    area = models.ForeignKey('areas', on_delete=models.CASCADE)
    fecha = models.DateField('Fecha')
    porcentaje = models.FloatField()

    IdAlumno= models.ForeignKey(
        'UsuarioAlumnos',
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f'{self.pk}'

class estadisticasPreguntas(models.Model):
    IdEstadistica= models.ForeignKey(
        'Estadisticas',
        on_delete=models.CASCADE,
        default=1
    )
    IdPregunta= models.ForeignKey(
        'repPreguntas',
        on_delete=models.CASCADE,
        default=1
    )
    def __str__(self):
        return f'{self.IdEstadistica},{self.IdPregunta}'

class repPreguntas(models.Model):
    pregunta= models.TextField('Preguntas',  max_length=5000)
    
    IdArea= models.ForeignKey(
        'areas',
        on_delete=models.CASCADE,
        default=1
    )
    def __str__(self):
        return f'{self.pregunta},{self.IdArea}'
    
    def get_respuestas(self):
        return self.respuestas_set.all()

class respuestas(models.Model):
    respuesta = models.CharField('Respuestas', max_length=1000)
    correcta = models.BooleanField(default=False)
    preguntas = models.ForeignKey(repPreguntas, on_delete=models.CASCADE)

    
    def __str__(self):
        return f"pregunta: {self.preguntas.pregunta},respuestas:{self.respuesta}, correcta:{self.correcta}"




class temas(models.Model):
    temaNombre = models.CharField('Tema', max_length=100, unique=True)
    informacion = models.TextField('Informacion', max_length=5000) 
    videolink=models.URLField('Link')
    imagen = models.FileField('Imagen')
    IdArea= models.ForeignKey(
        'areas',
        on_delete=models.CASCADE,
        default=1
    )
    def __str__(self):
        return f'{self.temaNombre},{self.IdArea}'

    def get_videos(self):
        return self.videos_set.all()


class areas(models.Model):
    nombreArea = models.CharField('Area', max_length=100, unique=True)
    informacion = models.TextField('Informacion', max_length=5000)

    def __str__(self):
        return f'{self.nombreArea}'
    
    def get_preguntas(self):
        return self.preguntas_set.all()

class ejemplos(models.Model):
    titulo = models.CharField('Titulo', max_length=100, unique=True)
    contenido= models.TextField('Contenido', max_length=5000)

    def __str__(self):
        return f'{self.titulo}'