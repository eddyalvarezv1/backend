from django.urls import path
from .views import (mostrarProductosPlantilla, crearProductosFormularios)


# para definir

urlpatterns = [
    path('mostrar-productos', mostrarProductosPlantilla, name='mostrar_productos'),
    path('crear-producto', crearProductosFormularios, name='crear_producto')
]