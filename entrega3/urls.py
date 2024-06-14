from django.urls import path
from entrega3 import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('juego/crear/', views.crearjuego2, name='crearjuego2'),
    path('juego/', views.juegos, name='juegos'),
]