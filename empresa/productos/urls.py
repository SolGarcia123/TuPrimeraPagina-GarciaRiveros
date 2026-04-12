from django.urls import path
from .views import ProductoList, ProductoDetail, ProductoCreate, ProductoUpdate, ProductoDelete, buscar_producto, productos_inicio

urlpatterns = [
    path('', productos_inicio, name='productos'),  
    path('lista/', ProductoList.as_view(), name='lista_productos'),
    path('crear/', ProductoCreate.as_view(), name='crear_producto'),
    path('<int:pk>/', ProductoDetail.as_view(), name='producto_detalle'),
    path('buscar/', buscar_producto, name='buscar_producto'),
    path('<int:pk>/editar/', ProductoUpdate.as_view(), name='editar_producto'),
path('<int:pk>/eliminar/', ProductoDelete.as_view(), name='eliminar_producto'),
]