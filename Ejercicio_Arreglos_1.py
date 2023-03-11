#Pseudocodigo y programa en C que lee un array de n*m elementos y que guarda en 0 en las posiciones pares. 
#y 1 en las posiciones impares. Imprimir el array resultante. 
#******************************************************************************************************

def posiciones():

    print ("Ingresar el número de la fila: ")
    filas=input()#Se solicita la cantidad de filas 

    if filas.isdigit()== True:
        filas=int(filas)#Se valida que lo ingresado en filas sea un dato numerico
        print("Ingresar el número de la columna:")
        columnas=input()#Se solicita la cantidad de columnas

        if columnas.isdigit()== True:
            columnas=int(columnas)#Se valida que lo ingresado en columnas sea un dato numerico
            matriz=[] #Se declara una array (lista)
                #Una matriz es una lista dentro de otra lista
            for i in range (filas):#Se recorre la filas
                matriz.append([])#Se esta creando una matriz. 

                for j in range (columnas):#Se recorre la columnas
                    if i == j:#Se valida que la posición de la fila sea igual a la columna 
                        matriz[i].append(0) #Si son iguales entonces se ingresa 0 en la posición que se esta recorriendo 
                    else: 
                        matriz[i].append(1)#Si no son iguales entonces se ingresa 1 en la posición que se esta recorriendo 

            for fila in matriz: #Se esta recorriendo la matriz y se desgloza en filas, se guarda la fila en esa posición 
                for valor in fila: #se recorre esa fila, las posiciones y en valor se tiene el valor de la fila que se esta iterando.
                    print ("\t", valor, end=" ")#Se imprime una matriz, se necesitan dos for
                print ()

        else:
            print ("El valor de la columna debe ser numerico")  #Alerta cuando se ingresa un dato mal, cuando se solicita la cantidad 
#de columnas.
    else:
        print ("El valor de la fila debe ser numerico")    #Alerta cuando se ingresa un dato mal, cuando se solicita la cantidad 
#de filas.

#******************************************************************
posiciones()