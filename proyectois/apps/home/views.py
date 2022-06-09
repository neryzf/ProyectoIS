from email import message
from multiprocessing import context
from django import forms
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.sessions.models import Session

# Create your views here.

class baseview(TemplateView):
    template_name='base.html'

class elementsview(TemplateView):
    template_name='elements.html'

class genericview(TemplateView):
    template_name='generic.html'

class indexcview(TemplateView):
    template_name='index.html'

class entrenamientoview(TemplateView):
    template_name='entrenamiento.html'

class resultadosview(TemplateView):
    template_name='resultados.html'

class homeView(TemplateView):
    template_name = 'home.html'

class loginView(LoginView):
    template_name = 'registro/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesion'
        return context


