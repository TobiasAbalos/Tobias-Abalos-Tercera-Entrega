from django.db import models


class Videojuego(models.Model):
    videojuego = models.CharField(max_length=20)
    productora = models.CharField(max_length=20)
    
    def __str__(self):
            return f'Juego: {self.videojuego}. Productora: {self.productora}.'
        
    


    
