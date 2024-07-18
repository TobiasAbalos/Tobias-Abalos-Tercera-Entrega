from django import forms

class CrearPais(forms.Form):
    pais = forms.CharField(max_length=20, required=False)
    capital = forms.CharField(max_length=20, required=False)
    ciudad = forms.CharField(max_length=20, required=False)
    municipio = forms.CharField(max_length=20, required=False)
    fecha = forms.DateField(required=False)
    
class CrearPaisFormulario(CrearPais):
    ...
    
class EditarPaisFormulario(CrearPais):
    ...
    
class BuscarPais(forms.Form):
    pais = forms.CharField(max_length=20, required=False)