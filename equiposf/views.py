from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Equipo
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q




class Equipos(ListView):
    model = Equipo
    template_name = 'equipos/lista_equipos.html'
    context_object_name = 'equipos'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formulario'] = BuscarEquipo(self.request.GET)
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        pais = self.request.GET.get('pais', None)
        liga = self.request.GET.get('liga', None)
        
        if pais:
            queryset = queryset.filter(pais__icontains=pais)
        if liga:
            queryset = queryset.filter(liga__icontains=liga)
            
        return queryset
    
class BuscarEquipo(forms.Form):
    pais = forms.CharField(max_length=20, required=False)
    liga = forms.CharField(max_length=20, required=False)
    
class CrearEquipo(CreateView):
    model = Equipo
    template_name ='equipos/crear_equipo.html'
    success_url = reverse_lazy('equipos')
    fields = ['equipo', 'pais', 'liga', 'fecha']
    
class EditarEquipo(LoginRequiredMixin, UpdateView):
    model = Equipo
    template_name ='equipos/editar_equipo.html'
    success_url = reverse_lazy('equipos')
    fields = ['equipo', 'pais', 'liga', 'fecha']
    
class VerEquipo(DetailView):
    model = Equipo
    template_name = 'equipos/ver_equipo.html'
    
class EliminarEquipo(LoginRequiredMixin, DeleteView):
    model = Equipo
    template_name = "equipos/eliminar_equipo.html"
    success_url = reverse_lazy('equipos')
    

