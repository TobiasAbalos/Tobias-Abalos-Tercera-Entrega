from django import forms

class CrearVideojuegos(forms.Form):
    videojuego = forms.CharField(max_length=20)
    productora = forms.CharField(max_length=20)
    