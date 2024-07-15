from django import forms

class CrearVideojuegos(forms.Form):
    videojuego = forms.CharField(max_length=20)
    productora = forms.CharField(max_length=20)
    
class CrearJuegoFormulario(CrearVideojuegos):
    ...
    
class EditarJuegoFormulario(CrearVideojuegos):
    ...
    
class BuscarJuego(forms.Form):
    productora = forms.CharField(max_length=20, required=False)