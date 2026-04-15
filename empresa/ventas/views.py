from django.shortcuts import render, redirect
from .models import Proveedor, Cliente
from .forms import ProveedorForm, ClienteForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Página principal
def inicio(request):
    return render(request, "ventas/inicio.html")

@login_required

def crear_proveedor(request):
    form = ProveedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'ventas/crear_proveedor.html', {'form': form})


def crear_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'ventas/crear_cliente.html', {'form': form})


def buscar_cliente(request):
    nombre = request.GET.get("nombre")
    clientes = Cliente.objects.filter(nombre__icontains=nombre) if nombre else []
    return render(request, "ventas/buscar_cliente.html", {"clientes": clientes})

def buscar_proveedor(request):
    nombre = request.GET.get("nombre")
    proveedores = Proveedor.objects.filter(nombre__icontains=nombre) if nombre else []
    return render(request, "ventas/buscar_proveedor.html", {"proveedores": proveedores})

def proveedor_inicio(request):
    return render(request, "ventas/proveedor_inicio.html")

def cliente_inicio(request):
    return render(request, "ventas/cliente_inicio.html")

def about(request):
    return render(request, 'ventas/about.html')