from django.urls import path
from entrega3 import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # path('juego/crear/', views.crearjuego2, name='crearjuego2'),
    path('juego/', views.juegos, name='juegos'),
    path('aboutme/', views.aboutme, name='aboutme'),
    # 
    path('autos/crear/', views.crearjuego2, name='crearjuego2'),
    path('autos/editar_juego/<int:id>', views.editar_juego, name='editar_juego'),
    path('autos/eliminar_juego/<int:id>', views.eliminar_juego, name='eliminar_juego'),
    path('autos/ver_juego/<int:id>/', views.ver_juego, name='ver_juego'),
    
    
    
    
]