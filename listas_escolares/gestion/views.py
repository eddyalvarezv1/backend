from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from .serializers import ProductoSerializer

# Create your views here.

def mostrarProductosPlantilla(request):
    # request > toda la informacion desde el navegador
    print(request)
    data = [
        {
            'id': 1,
            'nombre': 'Lapiz Faber Castell',
            'descripcion': 'Lapiz B2'
        },
        {
            'id': 2,
            'nombre': 'Resaltador color amarillo',
            'descripcion': None
        }
    ]
    # podemos retornar un html para cuestiones en que la aplicacion sea un monolito
    return render(request, 'mostrar_productos.html', {'data': data, 'mensaje': 'Bienvenido!'})

def crearProductosFormularios(request):
    if request.method == 'POST':
        print('Quieren crear un producto')
        # como en teoria ya se agrego mi producto en la base datos entonces mandare un redireccionamiento a la vista de listar los productos
        return redirect('mostrar_productos')
    elif request.method == 'GET':
        return render(request, 'formulario_producto.html')
    
@api_view(http_method_names=['GET','POST'])
def validarFuncionamiento(request):
    # Este request que nos llega usando rest_framework es un request diferente a la de las plantillas, porque se usa la libreria
    if request.method == 'GET':
        # En DRF no se puede retornar un plantilla sino que se tiene que retornar una respuesta http y para se puede utilizar la clases Response
        return Response(data={
            'message': 'El servidor funciona exitosamente'
        })
    
    elif request.method == 'POST':
        #Para leer la información proveniente del body usamos el request.data
        print(request.data)
        return Response(data={
            'message': 'Informacion aceptada correctamente'
        })
    
class ProductosController(GenericAPIView):
    def get(self, request):
        # SELECT * FROM productos;
        productos = Producto.objects.all()
        # al momento de crear la instancia del seializador se le pasa la información y si es una lista se le coloca el parametro many=true para que lo pueda iterar
        serializador = ProductoSerializer(productos, many=True)
        serializador.data
        # si la información es correctamente serializada retornará la data
        return Response(data={
            'message': 'Los productos son',
            'content': serializador.data
        })
    
    def post(self, request):
        # la data proviene del request
        data = request.data
        serializador = ProductoSerializer(data=data)
        # ahora como queremos validar si esta información proveniente del cliente es valida usamos el metodo is_valid()
        if serializador.is_valid():
            # Usando model serializers es muy facil guardar la informacion en la bd
            # aca la data ya es valida para guardarse
            serializador.save()

            return Response(data={
                'message': 'Producto creado exitosamente'
            })
        else:
            # Si no es valida
            # Si la información no es valida, los campos del porque no lo es se guardará en el atributo errors
            return Response(data={
                'message': 'Error al crear el producto',
                'content': serializador.errors
            })
        
        
class ListarYCrearProductoController():
    # Para utilizar una vista generica se tiene que definir los siguientes requisitos
    # Como obtendra la información y la devolvera
    queryset = Producto.objects
    # Para indicar como tiene que validar y devolver la información proveniente de la bd
    serializer_class = ProductoSerializer
