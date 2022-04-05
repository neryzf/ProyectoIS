from django.shortcuts import render
from django.views.generic import TemplateView
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
