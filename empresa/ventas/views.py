from django.shortcuts import render, redirect
from .models import Proveedor, Cliente
from .forms import ProveedorForm, ClienteForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def inicio(request):
    return render(request, "ventas/inicio.html")

@login_required
def crear_proveedor(request):
    form = ProveedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('proveedor_inicio')
    return render(request, 'ventas/crear_proveedor.html', {'form': form})

@login_required
def crear_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cliente_inicio')
    return render(request, 'ventas/crear_cliente.html', {'form': form})

@login_required
def buscar_cliente(request):
    nombre = request.GET.get("nombre")

    clientes = []


    if nombre:
        clientes = Cliente.objects.filter(nombre__icontains=nombre)

    return render(request, "ventas/buscar_cliente.html", {
        "clientes": clientes,
        "nombre": nombre
    })

@login_required
def buscar_proveedor(request):
    nombre = request.GET.get("nombre")

    proveedores = []


    if nombre:
        proveedores = Proveedor.objects.filter(nombre__icontains=nombre)

    return render(request, "ventas/buscar_proveedor.html", {
        "proveedores": proveedores,
        "nombre": nombre
    })

@login_required
def proveedor_inicio(request):
    return render(request, "ventas/proveedor_inicio.html")

@login_required
def cliente_inicio(request):
    return render(request, "ventas/cliente_inicio.html")

def about(request):
    return render(request, 'ventas/about.html')

@login_required
def cliente_detail(request, id):
    cliente = Cliente.objects.get(id=id)
    nombre = request.GET.get("nombre")

    return render(request, "ventas/cliente_detail.html", {
        "cliente": cliente,
        "nombre": nombre
    })

@login_required
def proveedor_detail(request, id):
    proveedor = Proveedor.objects.get(id=id)
    nombre = request.GET.get("nombre")

    return render(request, "ventas/proveedor_detail.html", {
        "proveedor": proveedor,
        "nombre": nombre
    })

@login_required
def cliente_update(request, id):
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        nombre = request.GET.get("nombre")
        if nombre:
            return redirect(f"/buscar-cliente/?nombre={nombre}")
        return redirect("buscar_cliente")

    nombre = request.GET.get("nombre")
    return render(request, "ventas/cliente_update.html", {
        "form": form,
        "nombre": nombre
    })

@login_required
def proveedor_update(request, id):
    proveedor = Proveedor.objects.get(id=id)
    form = ProveedorForm(request.POST or None, instance=proveedor)

    if form.is_valid():
        form.save()
        nombre = request.GET.get("nombre")
        if nombre:
            return redirect(f"/buscar-proveedor/?nombre={nombre}")
        return redirect("buscar_proveedor")

    nombre = request.GET.get("nombre")
    return render(request, "ventas/proveedor_update.html", {
        "form": form,
        "nombre": nombre
    })

@login_required
def cliente_delete(request, id):
    cliente = Cliente.objects.get(id=id)

    if request.method == "POST":
        nombre = request.GET.get("nombre")
        cliente.delete()

        if nombre:
            return redirect(f"/buscar-cliente/?nombre={nombre}")
        return redirect("buscar_cliente")

    nombre = request.GET.get("nombre")
    return render(request, "ventas/cliente_confirm_delete.html", {
        "cliente": cliente,
        "nombre": nombre
    })

@login_required
def proveedor_delete(request, id):
    proveedor = Proveedor.objects.get(id=id)

    if request.method == "POST":
        nombre = request.GET.get("nombre")
        proveedor.delete()

        if nombre:
            return redirect(f"/buscar-proveedor/?nombre={nombre}")
        return redirect("buscar_proveedor")

    nombre = request.GET.get("nombre")
    return render(request, "ventas/proveedor_confirm_delete.html", {
        "proveedor": proveedor,
        "nombre": nombre
    })

@login_required
def reporte_clientes(request):
    nombre = request.GET.get("nombre")

    clientes = Cliente.objects.all()

    if nombre:
        clientes = clientes.filter(nombre__icontains=nombre)

    return render(request, "ventas/reporte_clientes.html", {
        "clientes": clientes,
        "nombre": nombre
    })

@login_required
def reporte_proveedores(request):
    nombre = request.GET.get("nombre")

    proveedores = Proveedor.objects.all()

    if nombre:
        proveedores = proveedores.filter(nombre__icontains=nombre)

    return render(request, "ventas/reporte_proveedores.html", {
        "proveedores": proveedores,
        "nombre": nombre
    })