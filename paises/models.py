from django.db import models
from datetime import date


class PaisModel(models.Model):
    pais = models.CharField(max_length=20)
    capital = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    municipio = models.CharField(max_length=20)
    fecha = models.DateField(default=date.today)
    
    def __str__(self):
            return f'Pais: {self.pais}. Capital: {self.capital}. Ciudad: {self.ciudad}, Municipio: {self.municipio}, Fecha: {self.fecha}'

