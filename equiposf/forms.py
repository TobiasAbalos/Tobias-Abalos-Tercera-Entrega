from django import forms

class EquipoForm(forms.Form):
    equipo = forms.CharField(max_length=20, required=False)
    pais = forms.CharField(max_length=250, required=False)
    liga = forms.CharField(max_length=250, required=False)