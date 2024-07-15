from django.shortcuts import render, redirect
from entrega3.models1 import Videojuego
from django import forms
from entrega3.forms import CrearVideojuegos, BuscarJuego, EditarJuegoFormulario, CrearJuegoFormulario
import random
from datetime import datetime
def inicio(request):
    return render(request, 'inicio/index.html')

def crearjuego2(request):
    formulario = CrearJuegoFormulario()
       
    if request.method == 'POST':
        formulario = CrearJuegoFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            videojuego = Videojuego(videojuego=datos.get('videojuego'), productora=datos.get('productora'))
            videojuego.save()
            return redirect('juegos')
            
            
    
    return render(request, 'inicio/crearjuego2.html', {'formulario': formulario})

# def juegos(request):
    
#     juegos = Videojuego.objects.all()
    
#     return render(request, 'inicio/juegos.html', {'juegos':juegos})

def aboutme(request):
    return render(request, 'inicio/aboutme.html')

def juegos(request):
    
    formulario = BuscarJuego(request.GET)
    if formulario.is_valid():
        productora = formulario.cleaned_data['productora']
        juegos = Videojuego.objects.filter(productora__icontains=productora)
    
    # autos = Auto.objects.all()
    
    return render(request, 'inicio/juegos.html', {'juegos': juegos, 'formulario': formulario})

    


    