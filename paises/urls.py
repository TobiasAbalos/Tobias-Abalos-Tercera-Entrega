from django.urls import path
from paises import views

urlpatterns = [
    path('pais/', views.paises, name='paises'),
    path('paises/crear/', views.crearpais, name='crearpais'),
    path('juegos/editar_pais/<int:id>', views.editar_pais, name='editar_pais'),
    path('juegos/eliminar_pais/<int:id>', views.eliminar_pais, name='eliminar_pais'),
    path('juegos/ver_pais/<int:id>/', views.ver_pais, name='ver_pais'),
    
    
    
    
]