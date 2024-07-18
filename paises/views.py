from django.shortcuts import render, redirect
from paises.models import PaisModel
from paises.forms import CrearPaisFormulario, BuscarPais, EditarPaisFormulario, CrearPais
from django.contrib.auth.decorators import login_required


def crearpais(request):
    formulario = CrearPaisFormulario()
       
    if request.method == 'POST':
        formulario = CrearPaisFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            pais = PaisModel(pais=datos.get('pais'),
                             capital=datos.get('capital'),
                             ciudad=datos.get('ciudad'),
                             municipio=datos.get('municipio'),
                             fecha=datos.get('fecha'))
            pais.save()
            return redirect('paises')
        
    return render(request, 'pais/crearpais.html', {'formulario': formulario})

def paises(request):
    
    formulario = CrearPais(request.GET)
    paises = []
    if formulario.is_valid():
        capital = formulario.cleaned_data['capital']
        ciudad = formulario.cleaned_data['ciudad']
        municipio = formulario.cleaned_data['municipio']
        paises = PaisModel.objects.filter(capital__icontains=capital, ciudad__icontains=ciudad, municipio__icontains=municipio,)
    
    return render(request, 'pais/paises.html', {'paises': paises, 'formulario': formulario})

@login_required
def eliminar_pais(request, id):
    pais = PaisModel.objects.get(id=id)
    pais.delete()
    return redirect('paises')

@login_required
def editar_pais(request, id):
    pais = PaisModel.objects.get(id=id)
    formulario = EditarPaisFormulario(initial={'capital': pais.capital})
    if request.method == 'POST':
        formulario = EditarPaisFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            pais.capital = info['capital']
            pais.ciudad = info['ciudad']         
            pais.municipio = info['municipio']         
            pais.save()
            return redirect('paises')
        
    return render(request, 'pais/editar_pais.html', {'formulario' : formulario, 'pais':pais})

def ver_pais(request, id):
    pais = PaisModel.objects.get(id=id)
    return render(request, 'pais/ver_pais.html', {'pais':pais})