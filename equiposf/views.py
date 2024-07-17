from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Equipo
from django.urls import reverse_lazy
# from equiposf.forms import
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin




class Equipos(ListView):
    model = Equipo
    template_name = 'equipos/lista_equipos.html'
    context_object_name = 'equipos'
    def equipos(request):
        formulario = BuscarEquipo(request.GET)
        if formulario.is_valid():
            pais = formulario.cleaned_data['pais']
            liga = formulario.cleaned_data['liga']
            equipos = Equipo.objects.filter(liga_icontains=liga, pais_icontais=pais)
            
        return render(request, 'equiposf/lista_equipos.html', {'equipos':equipos, 'formulario':formulario})
    
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
    

