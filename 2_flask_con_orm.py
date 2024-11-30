from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, types
from flask_migrate import Migrate
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.exceptions import ValidationError



app= Flask(__name__)

# Aca agregamos la variable de conexion a  nuestra base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://postgres:root@localhost:5432/bd_flask'

conexion = SQLAlchemy(app=app)

Migrate(app=app, db = conexion)




# Cada tabla que vayamos a crear sera como una clase
class ProductoModel(conexion.Model):
    # Herencia: Semana 1 Programacion Orientada a Objetos
    # ahora declaramos las columnas de la tabla como si fueran atributos de la clase

    # id ....serial primary key  > SQL
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    # nombre ... not null, > SQL
    nombre = Column(type_=types.Text, nullable=False)
    # precio ... not null > SQL
    precio = Column(type_=types.Float(precision=2), nullable=False)
    # serie ... not null unique > SQL
    serie = Column(type_=types.Text, nullable=False, unique=True)
    disponible = Column(type_=types.Boolean, nullable=True)
    fechaVencimiento = Column(type_=types.Date, nullable=True)
    #name > si queremos manejar un nombre em el backend y otro nombre en la bd con la propiedad name indicamen como se llamará en la bd
    fechaVencimiento = Column(
        type_=types.Date, nullable=True, name='fecha_vencimiento')
    
    #para modificar el nombre de la tabla sin modificar le nombre de la clase
    __tablename__ = 'productos'


class ProductosSchema(SQLAlchemyAutoSchema):
    class Meta:
        #Sirve para pasarle informacion a la clase de la cual estamos heredando pero sin la necesidad de modificar como tal la instancia de la clase
        model = ProductoModel
        # al indicar el modelo que se tiene que basar podría ubicar todos los atributos y ver sus restricciones (not null, unico, tipo de datos, etc)


# @app.route('/crear-tablas')
# def crear_tablas():
    # creara todas la tablas que no esten en la base de datos
    #conexion.create_all()
    #return {
    #    'message': 'Las tablas fueron creadas exitosamente'
    #}

@app.route('/productos', methods=['POST', 'GET'])
def gestion_productos():
    metodo = request.method
    if metodo == 'POST':
        # primero leeremos la información proveniente del cliente
        # convierte el json entrante a un diccionario para que pueda ser leido en python
        data = request.get_json()

        # validara la informacion proveniente del frontend y nos dara un error si no cumple los requisitos

        try:
            serializador.load(data)

            # Inicializamos un nuevo registro
            nuevoProducto = ProductoModel(nombre=data.get('nombre'), 
                                        precio=data.get('precio'),
                                        serie=data.get('serie'),
                                        disponible=data.get('disponible'),
                                        fechaVencimiento=data.get('fechaVencimiento'))
            
            print('Producto antes de guardarse en la bd', nuevoProducto.id)
            # utilizamos la conexion para conectarnos a la bd
            # empezamos una transaccion en la cual estamos indicando que agregaremos este registro
            conexion.session.add(nuevoProducto)

            # indicamos que los cambios tiene que guardarse de manera permanente
            conexion.session.commit()

            print('Producto luego de guardarse en la bd', nuevoProducto.id)
            return {
                'message': 'Producto creado exitosamente'
            }
        
        except ValidationError as error:
            # si falla al momento de hacer la validación con el serializador
            return {
                'message':'Producto creado exitosamente',
                'content': error.args
            }

        except IntegrityError as error:
            #si falla al momento de guardar en la base de datos y el producto ya existe (nombre es unico)
            return {
                'message': 'Error al crear el proyecto',
                'content': 'El producto ya existe!'
            }


    elif metodo == 'GET':

        # Establecemos una consulta de obtencion de datos
        # SELECT * FROM productos:
        productos = conexion.session.query(ProductoModel).all()

        serializador = ProductosSchema()
        # cuando convertimos la informacion desde la bd a un dict utilizamos el metodo dump
        # cuando pasamos un arreglo de instancias tenemos que agregar el parametro many=true
        # ese parametro ayuda a que itere la lista y convierta cada uno de las instancias

        resultado = serializador.dump(productos, many=True)

        # print(productos)
        # print(productos[0].id)
        #convertir la informacion de la lista de instancias a diccionario
        #{
        #'id':1,
        #'nombre':'Ayudin',
        #...
        #}

        # resultado = []

        # for producto in productos:
        #     producto_dict = {
        #         'id': productos.id,
        #         'nombre': productos.nombre,
        #         'precio': productos.precio,
        #         'serie': productos.serie,
        #         'disponible': productos.disponible,
        #         'fechaVencimiento': productos.fechaVencimiento,
        #     }
        #     resultado.append(producto_dict)

        print(informacion_cliente)
        resultado.append(informacion_cliente)

        return {
            'message': 'los productos son',
            'content': resultado
        }


if __name__ == "__main__":
    app.run(debug=True)