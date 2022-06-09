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
from django import views
from django.contrib import admin
from django.urls import path,include

from .views import baseview, consultasView,elementsview, examenView,genericview, homeView, indexcview, entrenamientoview, loginView, resultadosview

urlpatterns = [
    path('base/', baseview.as_view(), name='base'),
    path('elements/', elementsview.as_view(), name='elements'),
    path('generic/', genericview.as_view(), name='generic'),
    path('index/', indexcview.as_view(), name='index'),
    path('entrenamiento/', entrenamientoview.as_view(), name='entrenamiento'),
    path('resultados/', resultadosview.as_view(), name='resultados'),
    path('home/', homeView.as_view(), name='home'),
    path('login/', loginView.as_view(), name='login'),
    path('examen/', examenView.as_view(),name='examen'),
    path('consulta/', consultasView.as_view(), name='consutla'),

]