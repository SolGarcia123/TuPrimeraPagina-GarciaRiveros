from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductoList(LoginRequiredMixin,ListView):
    model = Producto
    template_name = "productos/productos.html"

class ProductoDetail(LoginRequiredMixin,DetailView):
    model = Producto
    template_name = "productos/producto_detalle.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nombre"] = self.request.GET.get("nombre")
        return context


class ProductoCreate(LoginRequiredMixin,CreateView):
    model = Producto
    fields = '__all__'
    template_name = "productos/producto_form.html"
    success_url = reverse_lazy('productos')

class ProductoBusqueda(LoginRequiredMixin, ListView):
    model = Producto
    template_name = "productos/buscar_producto.html"
    context_object_name = "productos"

    def get_queryset(self):
        nombre = self.request.GET.get("nombre")

        if nombre:
            return Producto.objects.filter(nombre__icontains=nombre)

        return Producto.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.GET.get("nombre")
        return context


class ProductoUpdate(LoginRequiredMixin,UpdateView):
    model = Producto
    fields = '__all__'
    template_name = "productos/producto_update.html"
    success_url = reverse_lazy('buscar_producto')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nombre"] = self.request.GET.get("nombre")
        return context
    
    def get_success_url(self):
        nombre = self.request.GET.get("nombre")
        if nombre:
            return f"{reverse_lazy('buscar_producto')}?nombre={nombre}"
        return reverse_lazy('buscar_producto')    

class ProductoDelete(LoginRequiredMixin,DeleteView):
    model = Producto
    template_name = "productos/producto_confirm_delete.html"
    success_url = reverse_lazy('buscar_producto')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nombre"] = self.request.GET.get("nombre")
        return context
    
    def get_success_url(self):
        nombre = self.request.GET.get("nombre")
        if nombre:
            return f"{reverse_lazy('buscar_producto')}?nombre={nombre}"
        return reverse_lazy('buscar_producto')       

class ProductoReporte(LoginRequiredMixin, ListView):
    model = Producto
    template_name = "productos/reporte_productos.html"
    context_object_name = "productos"

    def get_queryset(self):
        nombre = self.request.GET.get("nombre")

        if nombre:
            return Producto.objects.filter(nombre__icontains=nombre)
        return Producto.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nombre"] = self.request.GET.get("nombre")
        return context