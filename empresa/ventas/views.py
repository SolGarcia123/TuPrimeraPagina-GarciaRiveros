from django.shortcuts import render, redirect
from .models import Proveedor, Cliente, Baldosa
from .forms import ProveedorForm, ClienteForm, BaldosaForm

# Página principal
def inicio(request):
    return render(request, "inicio.html")

# Formulario para crear proveedor
def crear_proveedor(request):
    form = ProveedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'crear_proveedor.html', {'form': form})

# Formulario para crear cliente
def crear_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'crear_cliente.html', {'form': form})

# Formulario para crear baldosa
def crear_baldosa(request):
    form = BaldosaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'crear_baldosa.html', {'form': form})

# Formulario para buscar clientes
def buscar_cliente(request):
    query = request.GET.get('q')
    resultados = Cliente.objects.filter(nombre__icontains=query) if query else []
    return render(request, 'buscar_cliente.html', {'resultados': resultados})
