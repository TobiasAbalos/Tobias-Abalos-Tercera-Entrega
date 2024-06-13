from django.db import models


class Videojuego(models.Model):
    videojuego = models.CharField(max_length=20)
    productora = models.CharField(max_length=20)
    
    def __str__(self):
            return f'Soy el juego {self.videojuego} {self.productora}'
        
    


    
