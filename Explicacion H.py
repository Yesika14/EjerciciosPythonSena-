##Modificar una lista
listadoUsurios = []

def agregarUsuario():
    usuario = {
        "Nombre":str(input("Ingrese el nombre: ")),
        "Apellido":str(input("Ingrese el apellido: ")),
    }
    listadoUsurios.append(usuario)
    print()
    menu2()

def mostrarUsuarios():
    for i in range(len(listadoUsurios)):
        print(i + 1, ") ", listadoUsurios[i]["Nombre"], listadoUsurios[i]["Apellido"])
    print()
    menu2()

def modificarUsuario():
    print("Seleccione el usurio que desea modificar")
    for i in range(len(listadoUsurios)):
        print(i + 1, ") ", listadoUsurios[i]["Nombre"], listadoUsurios[i]["Apellido"])
    usuarioSeleccionado = int(input())
    listadoUsurios[usuarioSeleccionado-1]["Nombre"] = str(input("Ingrese el nombre: "))
    listadoUsurios[usuarioSeleccionado-1]["Apellido"] = str(input("Ingrese el apellid: "))
    print()
    menu2()

def menu2():
    print("Selecione una opcion")  
    print("1) Ingresar usuario")
    print("2) Modificar usuario")
    print("3) Ver usuarios")
    print("4) Salir")
    opcion = int(input())
    if opcion == 1:
        agregarUsuario()
    if opcion == 2:
        modificarUsuario()
    if opcion == 3:
        mostrarUsuarios()
    if opcion == 4:
        print("Saliedo de la aplicación")
    if opcion > 4:
        print("Opcion no valida")
        menu2()