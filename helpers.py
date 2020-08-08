import random


def cargar_terreno():
    """Obtiene el terreno de un archivo .txt

    :return: Una matriz de enteros que representa el terreno
    """
    # Inicializar el terreno
    terreno = [[0 for i in range(20)] for i in range(20)]
    # Open file
    fila_terreno = open("./_resources/terreno.txt","r")
    if fila_terreno.mode == "r":
        lineas = fila_terreno.read().splitlines()
        fila = 0
        for linea in lineas:
            tiles = linea.split(",")
            columna = 0
            for tile in tiles:
                terreno[fila][columna] = int(tile)
                columna += 1
            fila += 1
    return terreno


def flip(prob):
    """Verifica si una probabilidad se cumple

    :param prob: La probabilidad que se desea verificar
    :return: Si se cumple dicha probabilidad
    """
    if random.random() < prob:
        return True
    else:
        return False
