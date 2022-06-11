"""proyectois URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import NamedNodeMap
from django import views
from django.contrib import admin
from django.urls import path,include

from .views import *
urlpatterns = [
    path('base/', baseview.as_view(), name='base'),
    path('elements/', elementsview.as_view(), name='elements'),
    path('generic/', genericview.as_view(), name='generic'),
    path('index/', indexcview.as_view(), name='index'),
    path('entrenamiento/', entrenamientoview.as_view(), name='entrenamiento'),

    path('material/', materialview.as_view(), name='material'),
    path('malgebra/', temaslist1.as_view(), name='malgebra'),
    path('mconjuntos/', temaslist2.as_view(), name='mconjuntos'),
    path('mtrigo/', temaslist3.as_view(), name='mtrigo'),
    path('mari/', temaslist4.as_view(), name='mari'),
    path('detalle/<int:pk>/', detallelist.as_view(), name='detalle'),

    path('resultados/', resultadosview.as_view(), name='resultados'),
    path('resal/', resultalg.as_view(), name='resal'),
    path('rescon/', resultcon.as_view(), name='rescon'),
    path('restri/', resultrigo.as_view(), name='restri'),
    path('resari/', resultari.as_view(), name='resari'),





    path('home/', homeView.as_view(), name='home'),
    path('login/', loginView.as_view(), name='login'),
    path('examen/', examenView.as_view(),name='examen'),


    path('preguntas/<int:pk>/', preguntasView, name='preguntasView'),
    path('preguntas/<int:pk>/data/', preguntasDatosView, name = 'quiz-data-view'),
    path('preguntas/<int:pk>/save/',save_quiz_view, name='save-view'),
    # path('preguntas/', preguntas.as_view(), name='preguntas'),
]