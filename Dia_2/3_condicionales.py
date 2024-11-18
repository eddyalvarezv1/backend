numero1 = 60
numero2 = 60

#     40   >    60   -> F
if numero1 > numero2:
    # si la condicion se cumple
    print('en efecto se debe agregar a la bd')
elif numero1 == numero2:
    # si la primera condicion no se cumple podemos hacer una segunda validacion
    print('no debemos hacer nada')
# elif ...
else:
    # si la condicion no se cumplio
    print('debemos solicitar los registros')


num_ventas = 30

if num_ventas >= 50:
    print('dscto del 20%')
elif num_ventas >= 30:
    print('dscto del 10%')
elif num_ventas >= 20:
    print('dscto del 5%')
else:
    print('dscto del 2%')


# crear una funcion llamada resultado_final en la cual se reciba el nombre del alumno y su nota
# si la nota es entre 20 y 18 entonces el alumno tiene felicitacion publica
# si la nota es entre 15 y 17 el alumno esta aprobado y exonerado de la exposicion final
# si la nota es entre 11 y 14 el alumno esta aprobado
# si la nota es menor o igual que 10 entonces el alumno esta jalado

# al final retornar un mensaje diciendo 'El alumno EDUARDO esta 'aprobado y exonerado de la exposicion final' > 15 y 17
# deadline Miercoles 20/11 18:59:59:59



alumnos = {
    "notas":[{
        "Eduardo":20,
        "Juan":16,
        "Mateo":13,
        "Jaime":9,
     }
    ],
}


def resultado_final(nombre):
    if  20 >= alumnos["notas"][0][nombre] and 18 <= alumnos["notas"][0][nombre]:
        print("El alumno", " ", nombre, " ", "recibirá felicitaciones pública y esta aprobado.")
    elif  17 >= alumnos["notas"][0][nombre] and 15 <= alumnos["notas"][0][nombre]:
        print("El alumno", " ", nombre, " ", "esta exonerado de la exposición y esta aprobado")
    elif  14 >= alumnos["notas"][0][nombre] and 11 <= alumnos["notas"][0][nombre]:
        print("El alumno", " ", nombre, " ", "esta aprobado")
    elif  10 >= alumnos["notas"][0][nombre] and 0 <= alumnos["notas"][0][nombre]:
        print("El alumno", " ", nombre, " ", "esta jalado")
    else:
        print("El alumno no pertenece a la clase")



resultado_final("Eduardo")
resultado_final("Juan")
resultado_final("Mateo")
resultado_final("Jaime")