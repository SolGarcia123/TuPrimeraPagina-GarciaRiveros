from django.contrib import admin
from django.urls import path
from ventas import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio),

    path('account/', include('account.urls')),
    
    path('crear-proveedor/', views.crear_proveedor),
    path('crear-baldosa/', views.crear_baldosa),
    path('buscar-baldosa/', views.buscar_baldosa),
    path('crear-cliente/', views.crear_cliente),
    path('buscar-cliente/', views.buscar_cliente),
    path('productos/', include('productos.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
