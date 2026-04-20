from django.urls import path
from .views import (
    ProductoList, ProductoDetail, ProductoCreate,
    ProductoUpdate, ProductoDelete, ProductoBusqueda, ProductoReporte
)


urlpatterns = [
    path('', ProductoList.as_view(), name='productos'),
    path('lista/', ProductoList.as_view(), name='lista_productos'),
    path('crear/', ProductoCreate.as_view(), name='crear_producto'),
    path('buscar/', ProductoBusqueda.as_view(), name='buscar_producto'),

    path('editar/<int:pk>/', ProductoUpdate.as_view(), name='producto_update'),
    path('<int:pk>/eliminar/', ProductoDelete.as_view(), name='producto_confirm_delete'),
    path('<int:pk>/', ProductoDetail.as_view(), name='producto_detalle'),
    path('reporte/', ProductoReporte.as_view(), name='reporte_productos'),
]