from django.shortcuts import render, redirect
from entrega3.models1 import Videojuego
from django import forms

from entrega3.forms import CrearVideojuegos

def inicio(request):
    return render(request, 'inicio/index.html')

def crearjuego2(request):
       
    if request.method == 'POST':
        formulario = CrearVideojuegos(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            videojuego = Videojuego(videojuego=datos.get('videojuego'), productora=datos.get('productora'))
            videojuego.save()
            return redirect('juegos')
            
            
    formulario = CrearVideojuegos()
    
    return render(request, 'inicio/crearjuego2.html', {'formulario': formulario})

def juegos(request):
    
    juegos = Videojuego.objects.all()
    
    return render(request, 'inicio/juegos.html', {'juegos':juegos})

    


    