from django.urls import path
from .views import (mostrarProductosPlantilla,
                    crearProductosFormularios,
                    validarFuncionamiento,
                    ProductosController,
                    ListarYCrearProductoController)


# para definir

urlpatterns = [
    path('mostrar-productos', mostrarProductosPlantilla, name='mostrar_productos'),
    path('crear-producto', crearProductosFormularios, name='crear_producto'),
    # no se recomienda definir un name porque no se hara un redireccionamiento hacia esta ruta al ser un API REST
    path('validar-funcionamiento', validarFuncionamiento),
    # Al momento de usar una clase de DRF tenemos que indicar que vamso a convertirla a una vista para que pueda entenderla django
    path('productos', ProductosController.as_view()),
    path('productos-v2', ListarYCrearProductoController.as_view())
]