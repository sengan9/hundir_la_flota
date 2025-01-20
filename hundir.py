import random

def crear_tablero(tamano):
    return [[0 for _ in range(tamano)] for _ in range(tamano)]

def crear_barco(longitud, tamano):
    orientacion = random.choice([0, 1])
    if orientacion == 0:
        fila = random.randint(0, tamano - 1)
        columna = random.randint(0, tamano - longitud)
    else:
        fila = random.randint(0, tamano - longitud)
        columna = random.randint(0, tamano - 1)
    return [(fila + i if orientacion else fila, columna if orientacion else columna + i) for i in range(longitud)]

def colocar_barco(barco, tablero):
    for (fila, columna) in barco:
        if fila >= len(tablero) or columna >= len(tablero[0]) or tablero[fila][columna] == 1:
            raise Exception("Barco fuera del tablero o colisión detectada")
        tablero[fila][columna] = 1
    return tablero

def disparar(coordenada, tablero):
    fila, columna = coordenada
    if tablero[fila][columna] == 1:
        print("¡Impacto!")
        tablero[fila][columna] = 2
        return True
    elif tablero[fila][columna] == 0:
        print("Agua")
        tablero[fila][columna] = -1
        return False
    else:
        print("Ya has disparado aquí")
        return False

def generar_disparo_aleatorio(tamano):
    return (random.randint(0, tamano - 1), random.randint(0, tamano - 1))

def todos_barcos_hundidos(tablero):
    for fila in tablero:
        if 1 in fila:
            return False
    return True

def jugar():
    tamano = 10
    tablero_jugador = crear_tablero(tamano)
    tablero_maquina = crear_tablero(tamano)

    barcos = [2, 3, 3, 4, 5]

    # Colocar barcos en el tablero del jugador
    for longitud in barcos:
        colocado = False
        while not colocado:
            try:
                barco = crear_barco(longitud, tamano)
                tablero_jugador = colocar_barco(barco, tablero_jugador)
                colocado = True
            except Exception:
                pass

    # Colocar barcos en el tablero de la máquina
    for longitud in barcos:
        colocado = False
        while not colocado:
            try:
                barco = crear_barco(longitud, tamano)
                tablero_maquina = colocar_barco(barco, tablero_maquina)
                colocado = True
            except Exception:
                pass

    turno_jugador = True
    while True:
        if turno_jugador:
            print("Tu turno")
            fila = int(input("Introduce la fila (0-9): "))
            columna = int(input("Introduce la columna (0-9): "))
            exito = disparar((fila, columna), tablero_maquina)
        else:
            print("Turno de la máquina")
            disparo = generar_disparo_aleatorio(tamano)
            print(f"Máquina dispara a {disparo}")
            exito = disparar(disparo, tablero_jugador)

        if todos_barcos_hundidos(tablero_maquina):
            print("¡Has ganado!")
            break
        elif todos_barcos_hundidos(tablero_jugador):
            print("¡La máquina ha ganado!")
            break

        turno_jugador = not turno_jugador

def imprimir_tablero(tablero, ocultar_barcos=False):
    simbolos = {
        0: ' ',  # Agua (sin disparar)
        1: 'B',  # Barco
        2: 'X',  # Impacto
        -1: 'O'  # Agua (disparada)
    }
    print("  " + " ".join(str(i) for i in range(len(tablero))))
    for idx, fila in enumerate(tablero):
        fila_visible = [simbolos[c] if not ocultar_barcos or c != 1 else ' ' for c in fila]
        print(f"{idx} " + " ".join(fila_visible))
    print()

# Inicia el juego
jugar()
