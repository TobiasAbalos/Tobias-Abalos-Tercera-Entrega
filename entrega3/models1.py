from django.db import models
from datetime import date


class Videojuego(models.Model):
    videojuego = models.CharField(max_length=20)
    productora = models.CharField(max_length=20)
    fecha = models.DateField(default=date.today)
    
    def __str__(self):
            return f'Juego: {self.videojuego}. Productora: {self.productora}.'
        
    


    
