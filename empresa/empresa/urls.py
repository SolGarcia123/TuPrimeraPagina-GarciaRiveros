from django.contrib import admin
from django.urls import path, include
from ventas import views as ventas_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', ventas_views.inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('about/', ventas_views.about, name='about'),
    path('account/', include('account.urls')),

   
    path('proveedor/', ventas_views.proveedor_inicio, name='proveedor_inicio'),
    path('crear-proveedor/', ventas_views.crear_proveedor, name='crear_proveedor'),
    path('buscar-proveedor/', ventas_views.buscar_proveedor, name='buscar_proveedor'),
    path('proveedor/<int:id>/', ventas_views.proveedor_detail, name='proveedor_detail'),
    path('proveedor/editar/<int:id>/', ventas_views.proveedor_update, name='proveedor_update'),
    path('proveedor/eliminar/<int:id>/', ventas_views.proveedor_delete, name='proveedor_confirm_delete'),
    path('proveedores/reporte/', ventas_views.reporte_proveedores, name='reporte_proveedores'),
    
    path('cliente/', ventas_views.cliente_inicio, name='cliente_inicio'),
    path('crear-cliente/', ventas_views.crear_cliente, name='crear_cliente'),
    path('buscar-cliente/', ventas_views.buscar_cliente, name='buscar_cliente'),
    path('cliente/<int:id>/', ventas_views.cliente_detail, name='cliente_detail'),
    path('cliente/editar/<int:id>/', ventas_views.cliente_update, name='cliente_update'),
    path('cliente/eliminar/<int:id>/', ventas_views.cliente_delete, name='cliente_confirm_delete'),
    path('clientes/reporte/', ventas_views.reporte_clientes, name='reporte_clientes'),
    
    path('productos/', include('productos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)