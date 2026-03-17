from django.contrib import admin
from django.urls import path
from ventas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio),

    # FORMULARIOS
    path('crear-proveedor/', views.crear_proveedor),
    path('crear-cliente/', views.crear_cliente),
    path('crear-baldosa/', views.crear_baldosa),
    path('buscar-baldosa/', views.buscar_baldosa),
    path('buscar-cliente/', views.buscar_cliente),
]