from django.shortcuts import render, HttpResponse

# Create your views here.

def indexcore(request): 
    return render(request, 'core/index.html')

def nosotros(request): 
    return render(request, 'core/nosotros.html')

def servicios(request): 
    return render(request, 'core/servicios.html')

def perfil(request): 
    return render(request, 'core/perfil.html')

def contacto(request): 
    return render(request, 'core/contacto.html')