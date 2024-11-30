from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError

class UsuarioSchema(Schema):
    nombre = fields.Str(required=True)
    apellido = fields.Str(required=True)
    correo = fields.Email()
    sexo = fields.Str(required=False)


usuario1 = { 'nombre':'Eduardo',
             'apellido':'Martinez',
             'correo':'emartinez@gmail.com',
            }

usuario2 = { 'nombre':'Roxana',
             'correo':'emartinez@gmail.com',
             'sexo': 'F'	
            }

validarUsuario = UsuarioSchema()

# load > validara la información que le estamos pasando con las propiedades del serializador y si algunas de las propiedades falta o no cumple entonce imitira un error
# por lo general se usa con un try-except
try:
    resultado = validarUsuario.load(usuario1)

    print(resultado)
except ValidationError as error: 
    # en todo error emitido para obtener el mensaje del error usamos el atributo args
    print(error.args)

try:
    resultado2 = validarUsuario.load(usuario2)
    print(resultado2)

except ValidationError as error:
    print(error.args)

class Usuario:
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo


nuevoUsuario = Usuario(
    nombre='Juancito',
    apellido='Gil',
    correo='jgil@gmail.com'
)

#dump > sirve para convertir informacion compleja como isntnacia de calses u 