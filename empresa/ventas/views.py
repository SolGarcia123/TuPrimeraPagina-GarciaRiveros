from django.shortcuts import render, redirect
from .models import Proveedor, Cliente, Baldosa
from .forms import ProveedorForm, ClienteForm, BaldosaForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Página principal
def inicio(request):
    return render(request, "ventas/inicio.html")

@login_required
# Formulario para crear proveedor
def crear_proveedor(request):
    form = ProveedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'ventas/crear_proveedor.html', {'form': form})

# Formulario para crear cliente
def crear_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'ventas/crear_cliente.html', {'form': form})

# Formulario para crear baldosa
def crear_baldosa(request):
    form = BaldosaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'ventas/crear_baldosa.html', {'form': form})

# Formulario para buscar clientes
def buscar_cliente(request):
    nombre = request.GET.get("nombre")
    clientes = Cliente.objects.filter(nombre__icontains=nombre) if nombre else []

    return render(request, "ventas/buscar_cliente.html", {"clientes": clientes})


def cliente_inicio(request):
    return render(request, "ventas/cliente_inicio.html")

def about(request):
    return render(request, 'ventas/about.html')