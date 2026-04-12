from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto
from django.urls import reverse_lazy
from django.shortcuts import render


class ProductoList(ListView):
    model = Producto
    template_name = "productos/productos.html"

class ProductoDetail(DetailView):
    model = Producto
    template_name = "productos/producto_detalle.html"


class ProductoCreate(CreateView):
    model = Producto
    fields = '__all__'
    template_name = "productos/producto_form.html"
    success_url = reverse_lazy('productos')

def buscar_producto(request):
    nombre = request.GET.get("nombre")
    productos = Producto.objects.filter(nombre__icontains=nombre) if nombre else []

    return render(request, "productos/buscar_producto.html", {
        "productos": productos,
        "nombre": nombre
    })

def productos_inicio(request):
    return render(request, "productos/productos.html")

class ProductoUpdate(UpdateView):
    model = Producto
    fields = '__all__'
    template_name = "productos/producto_form.html"
    success_url = reverse_lazy('productos')

class ProductoDelete(DeleteView):
    model = Producto
    template_name = "productos/producto_confirm_delete.html"
    success_url = reverse_lazy('productos')