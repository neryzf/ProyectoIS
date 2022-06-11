
from django.shortcuts import redirect, render
from django.views.generic import *
from django.contrib.auth.views import LoginView

from .models import *

from django.core.paginator import *


# Create your views here.

class baseview(TemplateView):
    template_name='base.html'

class elementsview(TemplateView):
    template_name='elements.html'

class genericview(TemplateView):
    template_name='generic.html'

class indexcview(TemplateView):
    template_name='index.html'



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

class examenView(TemplateView):
    template_name = 'examenapp.html'

""" class preguntas(ListView): 
    model = repPreguntas
    template_name = 'preguntas.html'
   
    paginate_by= 1
    
    def get_queryset(self, *args, **kwargs):

        qs = super(preguntas, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("?")[:15]

        
        return qs """
class entrenamientoview(ListView):
    model = areas
    template_name='entrenamiento.html'

def preguntasView(request, pk):
    quiz = areas.objects.get(pk=pk)
    return render(request, 'preguntas.html',{'obj':quiz})




class materialview(TemplateView):
    template_name='material.html'

class temaslist1(ListView):
    model = temas
    template_name = 'temasalg.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):

        qs = super(temaslist1, self).get_queryset(*args, **kwargs)
        qs = qs.filter(IdArea=1)


        return qs

class temaslist2(ListView):
    model = temas
    template_name = 'temasalg.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):

        qs = super(temaslist2, self).get_queryset(*args, **kwargs)
        qs = qs.filter(IdArea=2)


        return qs

class temaslist3(ListView):
    model = temas
    template_name = 'temasalg.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):

        qs = super(temaslist3, self).get_queryset(*args, **kwargs)
        qs = qs.filter(IdArea=3)


        return qs

class temaslist4(ListView):
    model = temas
    template_name = 'temasalg.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):

        qs = super(temaslist4, self).get_queryset(*args, **kwargs)
        qs = qs.filter(IdArea=4)


        return qs


class detallelist(DetailView):
    model = temas
    template_name = 'detalle.html'