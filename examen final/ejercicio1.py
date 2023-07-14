import random

def generar_lista_aleatoria():
    """Genera una lista de 10 números aleatorios entre 1 y 100."""
    lista = [random.randint(1, 100) for _ in range(10)]
    print("Lista de números aleatorios: ", lista)
    return lista

def eliminar_duplicados(lista):
    """Elimina los números duplicados de la lista."""
    lista_sin_duplicados = list(set(lista))
    print("Lista sin números duplicados: ", lista_sin_duplicados)
    return lista_sin_duplicados

def ordenar_listas(lista):
    """Ordena la lista de mayor a menor y de menor a mayor."""
    lista_menor_a_mayor = sorted(lista)
    lista_mayor_a_menor = sorted(lista, reverse=True)
    print("Lista ordenada de menor a mayor: ", lista_menor_a_mayor)
    print("Lista ordenada de mayor a menor: ", lista_mayor_a_menor)
    return lista_menor_a_mayor, lista_mayor_a_menor

def maximo_numero(lista):
    """Encuentra el número más grande de la lista."""
    maximo = max(lista)
    print("El número más grande de la lista es: ", maximo)
    return maximo

def main():
    lista_aleatoria = generar_lista_aleatoria()
    lista_sin_duplicados = eliminar_duplicados(lista_aleatoria)
    ordenar_listas(lista_sin_duplicados)
    maximo_numero(lista_sin_duplicados)

if __name__ == "__main__":
    main()
