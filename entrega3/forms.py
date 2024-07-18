from django import forms

class CrearVideojuegos(forms.Form):
    videojuego = forms.CharField(max_length=20)
    productora = forms.CharField(max_length=20)
    fecha = forms.DateField()
    
class CrearJuegoFormulario(CrearVideojuegos):
    fecha = forms.DateField()
    
class EditarJuegoFormulario(CrearVideojuegos):
    ...
    
class BuscarJuego(forms.Form):
    productora = forms.CharField(max_length=20, required=False)
    # fecha = forms.DateField()