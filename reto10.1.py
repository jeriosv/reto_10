def calcularPromedio(lista:list) -> float: # Función para calcular promedio
    suma = 0              # Inicializar promedio en 0
    for numero in lista:  # Realiza la suma de los números reales
        suma += numero
    return suma / len(lista) # Retorna el promedio

if __name__ == "__main__":
    n = int(input("Ingrese la cantidad de números reales a ingresar: "))   # Ingreso de cantidad de números
    lista = [float(input("Ingrese el número real No. " + str(x+1) + ": ")) for x in range(n)]  # Ingreso de los números reales
   
    respuesta = calcularPromedio(lista)  # Llamar la función y asignarlo a respuesta
    print("El promedio de " + str(lista) + " es: " + str(respuesta)) # Imprimir resultado