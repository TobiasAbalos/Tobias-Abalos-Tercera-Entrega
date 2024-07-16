from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Equipo
from django.urls import reverse_lazy


class Paletas(ListView):
    model = Equipo
    template_name = 'equipos/lista_equipos.html'
    context_object_name = 'equipos'
    
class CrearPaleta(CreateView):
    model = Equipo
    template_name ='equipos/crear_equipo.html'
    success_url = reverse_lazy('equipos')
    fields = ['equipo', 'pais', 'liga', 'fecha']
    
class EditarPaleta(UpdateView):
    model = Equipo
    template_name ='equipos/editar_equipo.html'
    success_url = reverse_lazy('equipos')
    fields = ['equipo', 'pais', 'liga', 'fecha']
    
class VerPaleta(DetailView):
    model = Equipo
    template_name = 'equipos/ver_equipo.html'
    
class EliminarPaleta(DeleteView):
    model = Equipo
    template_name = "equipos/eliminar_equipo.html"
    success_url = reverse_lazy('equipos')

# Create your views here.
