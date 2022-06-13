from tkinter import Widget
from django import forms
from . import models
#from django.contrib.auth.forms import  AuthenticationForm
from .models import UsuarioAlumnos

#Se crea el form para poder crear nuevos usuarios. Utilizo el modelo ya pre-creado
#El modelo que use se encuentra a partir de la linea 39 del directorio home/models.py
#El nombre del modelo es UsuarioAlumnos

class CrearUsuario(forms.ModelForm):
    password1 = forms.CharField(label = 'Ingrese su contraseña', widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'id': 'password1',
            'required': 'required',
        }
    ))

    password2 = forms.CharField(label = 'Ingrese nuevamente su contraseña', widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'id': 'password2',
            'required': 'required',
        }
    ))
    class Meta:
        model = UsuarioAlumnos
        fields = ['username','nombres','apellidos','email', 'IDSeccion', 'IDGrado']

    def clean_password2(self):
        #validacion de contraseña, valida que ambas contraseñas sean iguales
         #antes de encriptarlas y guardarlas en la BD

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden!')
        return password2
        
        #Aca se encripta la contraseña si el paso anterior fue validado correctamente
    def save(self,commit = True):
        usuario = super().save(commit = False) 
        usuario.set_password(self.cleaned_data['password1'])
        if commit:
            usuario.save()
        return usuario