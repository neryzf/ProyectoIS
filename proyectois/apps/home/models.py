from tkinter import CASCADE
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
    fecha = models.DateField('Fecha')
    porcentaje = models.DecimalField('Porcentaje', max_digits=5, decimal_places=2)

    IdAlumno= models.ForeignKey(
        'UsuarioAlumnos',
        on_delete=models.CASCADE,
        default=1
    )
    
    def __str__(self):
        return f'{self.IdAlumno},{self.porcentaje}'

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

class repPreguntas(models.Model):
    pregunta= models.TextField('Preguntas',  max_length=5000)

    Idrespuesta= models.ForeignKey(
        'respuestas',
        on_delete=models.CASCADE,
        default=1
    )
    
    IdTema= models.ForeignKey(
        'temas',
        on_delete=models.CASCADE,
        default=1
    )


class respuestas(models.Model):
    respuesta = models.TextField('Respuestas', max_length=1000)
    IdTema= models.ForeignKey(
        'temas',
        on_delete=models.CASCADE,
        default=1
    )



class temas(models.Model):
    temaNombre = models.CharField('Tema', max_length=100, unique=True)
    informacion = models.TextField('Informacion', max_length=5000) 
    IdArea= models.ForeignKey(
        'areas',
        on_delete=models.CASCADE,
        default=1
    )

class areas(models.Model):
    nombreArea = models.CharField('Area', max_length=100, unique=True)
    informacion = models.TextField('Informacion', max_length=5000)

class ejemplos(models.Model):
    titulo = models.CharField('Titulo', max_length=100, unique=True)
    contenido= models.TextField('Contenido', max_length=5000)

class videos(models.Model):
    nombre = models.CharField('Nombre Video', max_length=100, unique=True)
    link = models.URLField('Link')
    creditos = models.CharField('Creditos', max_length=200)


class imagens(models.Model):
    nombre = models.CharField('Nombre', max_length=100, unique=True)
    archivo = models.FileField('Archivo')
    creditos = models.CharField('Creditos', max_length=200)

    Idtema = models.ManyToManyField(temas)
