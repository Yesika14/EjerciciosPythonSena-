
#2. Crear un programa en donde se evidencie las tuplas.
#Dicho programa es para llevar el control de notas de estudiante (uno), 
#debe tener un menú de cuatro opciones (asignar notas, modificar notas y eliminar materia), 
#el programa debe solicitar el nombre del estudiante y las notas (p1, p2 y p3)
#***************************************************************************************

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print (clave + ") " + opciones[clave][0])
       
#*********************************************************

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

#*********************************************************
def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

#*********************************************************
def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()
       

#*********************************************************
def menu_principal():
    opciones = {
        '1': ('Asignar Notas', asignarnota),
        '2': ('Modificar Notas', modificarnotas),
        '3': ('Eliminar Materia', eliminarmateria),
        '4': ("Mostrar Alumnos", mostraralumnos),
        '5': ('Salir', "salir")
    }

    generar_menu(opciones, '5')

#*********************************************************

listadoalumnos=[]

def asignarnota():
    print("Digite el nombre del estudiante")
    nombre=str(input())
    print("Desea agregar materias, 1 (Si) 2 (No)")
    opcion=int(input())
    materias=[]
    while opcion == 1:
        print("Ingrese nombre de la materia")
        nombremateria=str(input())
        print ("Digite Nota 1: ")
        nota1=int(input())
        print ("Digite Nota 2: ")
        nota2=int(input())
        print ("Digite Nota 3: ")
        nota3=int(input())
        materia = {
            "Nombre" : nombremateria,
            "Notas" : (nota1,nota2,nota3)
        }
        materias.append(materia)
        print("Desea agregar otra materia, 1 (Si) 2 (No)")
        opcion=int(input())
    alumno = {
        "Nombre" : nombre, 
        "Materias" : materias
    }
    listadoalumnos.append(alumno)

#****************************************************************

def mostraralumnos():
    print ("listado de alumnos", listadoalumnos)

#*****************************************************************

def eliminarmateria():
    print("Seleccione alumno")
    for index,alumno in enumerate (listadoalumnos):
        print (index + 1,")", alumno["Nombre"])
    opcion=int(input())
    materias=listadoalumnos[opcion-1]["Materias"]
    print("Seleccione la materia que quiere eliminar")
    for indx, materia in enumerate (materias):
        print (indx + 1,")", materia["Nombre"])
    opcionmateria=int(input())
    materias.pop(opcionmateria-1)
    print("Se ha eliminado la materia con exito.")

#*****************************************************************

def modificarnotas():
    print("Seleccione alumno")
    for index,alumno in enumerate (listadoalumnos):
        print (index + 1,")", alumno["Nombre"])
    opcion=int(input())
    materias=listadoalumnos[opcion-1]["Materias"]
    print("Seleccione la materia a la cual desea modificar la nota")
    for indx, materia in enumerate (materias):
        print (indx + 1,")", materia["Nombre"])
    opcionmateria=int(input())
    print ("Digite Nota 1: ")
    nota1=int(input())
    print ("Digite Nota 2: ")
    nota2=int(input())
    print ("Digite Nota 3: ")
    nota3=int(input())
    materia = {
        "Nombre" : materias[opcionmateria-1]["Nombre"],
        "Notas" : (nota1,nota2,nota3)
    }
    materias[opcionmateria-1]=materia
    print("Las notas se han actualizado con exito.")

#*****************************************************************

menu_principal()