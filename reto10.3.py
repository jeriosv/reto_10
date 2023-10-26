def moverCeros(arreglo):    # Función que mueve los ceros al final del arreglo
    ceros = []
    i = 0                   # Inicializa contador 
    while i < len(arreglo): #  Itera según la longitud del arreglo 
        if arreglo[i] == 0: # Si un elemento es cero, se agrega a la lista ceros y se elimina de la original
            ceros.append(arreglo.pop(i)) # si es igual a cero se agrega a la lista ceros y se elimina de la original 
        else:               # sino se aumenta el contador
            i += 1
    arreglo.extend(ceros)   # Agregar los ceros al final del arreglo
    return arreglo

if __name__ == "__main__":
    n = int(input("Ingrese la cantidad de números a ingresar: "))   # Ingreso de cantidad de números
    arreglo= [int(input("Ingrese el número entero No. " + str(x+1) + ": ")) for x in range(n)]  # Ingreso de los números enteros
  
    print("El arreglo original es :       " + str(arreglo))  # Imprimir el arreglo original
    arreglo = moverCeros(arreglo) # Llamar la función y asignarlo a arreglo
    print("El arreglo con ceros al final: " + str(arreglo))  # Imprimir el arreglo con ceros al final