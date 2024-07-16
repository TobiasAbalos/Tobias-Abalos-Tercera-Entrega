from django.db import models

class Equipo(models.Model):
    equipo = models.CharField(max_length=20)
    pais = models.CharField(max_length=250)
    liga = models.CharField(max_length=250)
    fecha = models.DateField()
       
    def __str__(self):
        return f'{self.equipo} {self.pais} {self.liga} {self.fecha}'
