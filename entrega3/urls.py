from django.urls import path
from entrega3 import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('prueba/', views.probando, name='probando'),
    path('juego/crear/<str:videojuego>/<str:productora>', views.crearjuego, name='crearjuego'),
]