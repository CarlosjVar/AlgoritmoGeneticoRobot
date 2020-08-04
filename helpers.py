def cargar_terreno():
    terreno = [[0 for i in range(20)] for i in range(20)]
    fila_Terreno = open("./_resources/terreno.txt","r")
    if fila_Terreno.mode == "r":
        lineas = fila_Terreno.read().splitlines()
        fila = 0
        for linea in lineas:
            tiles = linea.split(",")
            columna = 0
            for tile in tiles:
                terreno[fila][columna] = int(tile)
                columna += 1
            fila += 1
    return terreno