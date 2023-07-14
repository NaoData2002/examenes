import random
import math


def crear_lista_aleatoria(tamano, rango_inferior=1, rango_superior=100):
    """Crea una lista de números aleatorios."""
    if tamano < 0 or rango_inferior > rango_superior:
        return []

    lista = [random.randint(rango_inferior, rango_superior) for _ in range(tamano)]
    return lista


def obtener_raices_cuadradas(lista):
    """Calcula la raíz cuadrada de cada número en la lista."""
    if not lista:
        return []

    raices = [math.sqrt(n) for n in lista]
    return raices


def main():
    """Función principal."""
    tamano = int(input("Ingrese el tamaño de la lista: "))
    lista = crear_lista_aleatoria(tamano)

    with open('notas.txt', 'w') as file:
        for num in lista:
            file.write(str(num) + '\n')

    raices = obtener_raices_cuadradas(lista)

    with open('notas.txt', 'a') as file:
        for raiz in raices:
            file.write(str(raiz) + '\n')


if __name__ == "__main__":
    main()
