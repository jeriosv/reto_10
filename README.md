# Reto No. 10:  Arreglos, listas.

## 1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

```python
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
```

## 2. Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

   "The dot product is one way of multiplying two or more vectors. The resultant of the dot product of vectors is a scalar quantity. Thus, the dot product is also known as a scalar product. Algebraically, it is the sum of the products of the corresponding entries of two sequences of numbers."
Tomado de https://www.cuemath.com/algebra/dot-product/

```python
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
```

## 3. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.

```python
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
```

## 4. Revisar que son los algoritmos de sorting, entender bubble-sort (enlace a implementación).

   El algoritmo de ordenamiento de burbuja (Bubble Sort en inglés) es un algoritmo simple que se utiliza para ordenar una lista o un arreglo de elementos. El nombre "burbuja" proviene del hecho de que los elementos más grandes "burbujean" hacia arriba a medida que se comparan y se intercambian a lo largo del arreglo, hasta que todos los elementos estén en su posición correcta.
   Bubble Sort es el algoritmo más simple de clasificación, que funciona intercambiando repetidamente los elementos adyacentes si están en el orden incorrecto. Este algoritmo no es adecuado para grandes conjuntos de datos por su complejidad promedio y toma ucho tiempo en procesamiento.
   En este algoritmo:
     - Se recorre desde la izquierda y compara los elementos adyacentes y el superior se coloca en el lado derecho. 
     - De esta manera, el elemento más grande se mueve primero hacia el extremo derecho. 
     - Luego se continúa con este proceso para encontrar el segundo más grande y colocarlo y así sucesivamente hasta que se ordenen los datos.

   ![image](https://github.com/jeriosv/reto_10/assets/142249529/67bed4a8-e425-49c6-8a97-57366a9d8ccc)


A continuación una implemetación del código fuente para bubble sorting:

```python
# Optimized Python program for implementation of Bubble Sort
  
def bubbleSort(arr):
    n = len(arr)
     
    # Traverse through all array elements
    for i in range(n):
        swapped = False
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
 
# Driver code to test above
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
 
    bubbleSort(arr)
 
    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
 
# This code is modified by Suraj krushna Yadav
```

Tomado de: https://www.geeksforgeeks.org/bubble-sort/
