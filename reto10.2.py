def calcularProductoPunto(vector1:list, vector2:list) -> float: # Función para calcular el producto punto
    productoPunto = 0           # Inicializa la variable en 0
    for i in range(len(vector1)): # Itera según la longitud del vector 1
        productoPunto += vector1[i]*vector2[i] # Va acumulando los productos (multiplicaciones)
    return productoPunto

if __name__ == "__main__":
    n = int(input("Ingrese el tamaño que tendrán los 2 vectores: "))
    vector1 = [float(input("Ingrese el número real No. " + str(x+1) + " del primer vector: ")) for x in range(n)]  # Ingreso de los números reales
    vector2 = [float(input("Ingrese el número real No. " + str(x+1) + " del segundo vector: ")) for x in range(n)]  # Ingreso de los números reales
    respuesta = calcularProductoPunto(vector1, vector2) # Llamar la función y asignarlo a respuesta
    print("El producto punto de", vector1, "y", vector2, "es:", respuesta) # Imprimir rsultado