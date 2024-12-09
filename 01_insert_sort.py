# Se crea la funciona o el algoritmo de insertsort 

def insertsort (array):
    # Se obtiene la longitud del array 
    length = len(array)
    # Se crea el bucle for comparando desde la posicion 1 hasta la ultima posision
    # Se compara de la posicion 1 por que el algoritmo determina que el primer elemento esta ordenado
    for i in range(1, length):
        # Se crea la variable insert_value que es igual al valor de dicha posicion
        insert_value = array[i]
        # Se crea la posicion en la cual se insertara el valor de cumplirse la condicion
        insert_index = i
        # Se crea un bulce while donde se compara primero que la posicion evaluada no se la 0 porque ese valor siempre estara ordenado 
        # Despues se compara el valor de la posicion anterior con el actual para ver si es mayor o menor 
        while insert_index > 0 and array[insert_index -1] > insert_value:
           # Se puede decir que el numero de la posicion actual se guarda en la posicionn a la izquierda
            array[insert_index] = array[insert_index -1]
            insert_index -= 1
        array[insert_index] = insert_value 
    return array

# Se crea una lista de numeros desordenados

puntos = [4, 3, 6, 2, 1, 5]

# En las siguientes lineas se imprime la lista creadas primero la desordenada y despues la ordenada

print(f"\n Antes de ordenar: {puntos} \n")
print (f"Despues de ordenar: {insertsort(puntos)}")