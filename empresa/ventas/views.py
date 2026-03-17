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
    nombre = request.GET.get("nombre")
    clientes = Cliente.objects.filter(nombre__icontains=nombre) if nombre else []

    return render(request, "buscar_cliente.html", {"clientes": clientes})

# Formulario para buscar baldosa
def buscar_baldosa(request):
    modelo = request.GET.get("modelo")
    baldosas = Baldosa.objects.filter(modelo__icontains=modelo) if modelo else []

    return render(request, "buscar_baldosa.html", {
        "baldosas": baldosas,
        "modelo": modelo
    })