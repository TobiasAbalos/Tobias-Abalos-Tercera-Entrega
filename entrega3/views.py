from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.http import HttpResponse
from django.template import Template, Context, loader
from django.db import migrations, models

from entrega3.models1 import Videojuego
from django import forms

# from entrega3.forms import CrearAuto, BuscarAuto

import random

def inicio(request):
    return render(request, 'inicio/index.html')

def probando(request):
    
    lista = list(range(500))
    
    numeros = random.choices(lista, k=50)
    print(numeros)
    return render(request, 'probando.html', {'numeros': numeros})

def crearjuego(request, videojuego, productora):
    juego = Videojuego(videojuego=videojuego, productora=productora)
    juego.save()
    return render(request, 'inicio/juegos.html', {'videojuego': videojuego})

    