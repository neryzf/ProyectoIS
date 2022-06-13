from cgi import print_form
from django.shortcuts import redirect, render
from django.views.generic import *
from django.contrib.auth.views import LoginView

from .forms import CrearUsuario

from .models import *

from django.core.paginator import *
from django.http import *

from django.shortcuts import *


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

class resultalg(ListView):
    model = Estadisticas
    template_name = 'resdetail.html'
    paginate_by = 1

    def get_queryset(self, *args, **kwargs):

        qs = super(resultalg, self).get_queryset(*args, **kwargs)
        qs = qs.filter(area=1)


        return qs

class resultcon(ListView):
    model = Estadisticas
    template_name = 'resdetail.html'
    paginate_by = 1

    def get_queryset(self, *args, **kwargs):

        qs = super(resultcon, self).get_queryset(*args, **kwargs)
        qs = qs.filter(area=2)


        return qs

class resultrigo(ListView):
    model = Estadisticas
    template_name = 'resdetail.html'
    paginate_by = 1

    def get_queryset(self, *args, **kwargs):

        qs = super(resultrigo, self).get_queryset(*args, **kwargs)
        qs = qs.filter(area=3)


        return qs

class resultari(ListView):
    model = Estadisticas
    template_name = 'resdetail.html'
    paginate_by = 1

    def get_queryset(self, *args, **kwargs):

        qs = super(resultari, self).get_queryset(*args, **kwargs)
        qs = qs.filter(area=4)


        return qs


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

def preguntasDatosView(request, pk):
    quiz= areas.objects.get(pk=pk)
    preg = []
    for q in quiz.get_reppreguntas():
        respuestas = []        
        
        for a in q.get_respuestass():
            respuestas.append(a.respuesta)           
        preg.append({str(q):respuestas})

    return JsonResponse({

        'data':preg
    })

def save_quiz_view(request, pk):
    #print(request.POST)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        preguntas=[]
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = repPreguntas.objects.get(pregunta=k)
            preguntas.append(question)
            
        
       

        user = request.user
        quiz = areas.objects.get(pk=pk)
        
        score =0
        multiplier = 100/10
        results = []
        correct_answer = None

        

        for q in preguntas:
            a_select= request.POST.get(q.pregunta)
            print('selected', a_select)
            

            if a_select != "":
                question_answers= respuestas.objects.get(preguntas_id = q)
                for a in question_answers:
                    if a_select == a.respuesta:
                        if a.correct:
                            score+=1
                            correct_answer = a.respuesta
                    else:
                        if a.correct:
                            correct_answer = a.respuesta

                results.append({str(q):{'correct_anserd':correct_answer,'answered':a_select}})

            else:
                results.append({str(q):{'not answerd':correct_answer,'answered':a_select}})
        
        score_ = score * multiplier

        Estadisticas.objects.create(area= quiz, IdAlumno = user, porcentaje =score_ )

    return JsonResponse({'text':'work'})



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

#Permite poder habilitar el view para crear el formulario de creacion de usuario
def Crear(request):
    form = CrearUsuario()

    if request.method == "POST":
        form = CrearUsuario(request.POST)

        if form.is_valid():
            print("Valido")
            form.save()
            form.cleaned_data
            return redirect('index')
        else:
            form = CrearUsuario()
            print("Invalido")

    return render(request,'registro/crear.html',{'form': form})