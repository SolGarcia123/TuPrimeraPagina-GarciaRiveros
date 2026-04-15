from django.contrib import admin
from django.urls import path
from ventas import views as ventas_views
from productos import views as productos_views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', ventas_views.inicio),
    path('admin/', admin.site.urls),
    path('about/', ventas_views.about),
    path('account/', include('account.urls')),

    path('proveedor/', ventas_views.proveedor_inicio, name='proveedor_inicio'),
    path('crear-proveedor/', ventas_views.crear_proveedor),
    path('buscar-proveedor/', ventas_views.buscar_proveedor, name='buscar_proveedor'),
    
    path('cliente/', ventas_views.cliente_inicio, name='cliente_inicio'),
    path('crear-cliente/', ventas_views.crear_cliente),
    path('buscar-cliente/', ventas_views.buscar_cliente),

    path('productos/', include('productos.urls')),
    path('crear-producto/', productos_views.ProductoCreate.as_view(), name='crear_producto'),
    path('buscar-producto/', productos_views.buscar_producto),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
