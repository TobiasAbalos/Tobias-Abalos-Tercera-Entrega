from django.urls import path
from entrega3 import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # path('juego/crear/', views.crearjuego2, name='crearjuego2'),
    path('juego/', views.juegos, name='juegos'),
    path('aboutme/', views.aboutme, name='aboutme'),
    # 
    path('juegos/crear/', views.crearjuego2, name='crearjuego2'),
    path('juegos/editar_juego/<int:id>', views.editar_juego, name='editar_juego'),
    path('juegos/eliminar_juego/<int:id>', views.eliminar_juego, name='eliminar_juego'),
    path('juegos/ver_juego/<int:id>/', views.ver_juego, name='ver_juego'),
    
    
    
    
]