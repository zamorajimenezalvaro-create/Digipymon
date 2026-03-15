import random

from Digipymon import Digipymon
from Jugador import Jugador
from Enemigo import Enemigo
from Inventario import Inventario
from ListaNombres import ListaNombres

lista_nombres = ListaNombres()


def generar_digipymon_aleatorio():
    """
    Genera un Digipymon con estadísticas aleatorias.

    Returns
    -------
    Digipymon
        Un Digipymon generado aleatoriamente.
    """
    vida = random.randint(10, 20)
    ataque = random.randint(1, 10)
    nivel = random.randint(1, 3)
    tipo = random.choice(["fuego", "agua", "planta"])
    nombre = lista_nombres.obtener_nombre_digipymon()

    return Digipymon(nombre, vida, ataque, tipo, nivel)


def menu():
    """
    Muestra el menú principal y solicita una opción al usuario.

    Returns
    -------
    str
        Opción elegida por el usuario.
    """
    print("\n--- MENÚ ---")
    print("1. Buscar Digipymon")
    print("2. Luchar contra un entrenador")
    print("3. Ir a la tienda")
    print("4. Usar objetos")
    print("5. Consultar inventario")
    print("6. Consultar digipymons")
    print("7. Salir")

    return input("Elige una opción: ")


def buscar_digipymon(jugador, inventario):
    """
    Permite al jugador encontrar y capturar un Digipymon salvaje.

    Parameters
    ----------
    jugador : Jugador
        Jugador actual.
    inventario : Inventario
        Inventario del jugador.
    """
    digipymon = generar_digipymon_aleatorio()

    print("\nHas encontrado un Digipymon:")
    print(digipymon)

    probabilidad = 100 - (digipymon.nivel * 10)
    print("Probabilidad de captura:", probabilidad, "%")

    decision = input("¿Quieres capturarlo? (s/n): ")

    if decision.lower() == "s":

        if "digipyball" not in inventario.objetos or inventario.objetos["digipyball"] <= 0:
            print("No tienes digipyballs.")
            return

        if jugador.cantidad_digipymon >= 6:
            print("Tu equipo está lleno.")
            return

        inventario.usar_objeto("digipyball")

        intento = random.randint(1, 100)

        if intento <= probabilidad:
            print("¡Has capturado al Digipymon!")
            jugador.añadir_digipymon(digipymon)
        else:
            print("El Digipymon escapó.")

    else:
        print("Has huido.")


def combate(jugador):
    """
    Gestiona un combate entre el jugador y un entrenador enemigo.

    Parameters
    ----------
    jugador : Jugador
        Jugador que participa en el combate.
    """
    nombre = lista_nombres.obtener_nombre_entrenador()
    enemigo = Enemigo(nombre)

    print("\nTe enfrentas al entrenador:", nombre)

    for _ in range(jugador.cantidad_digipymon):
        enemigo.añadir_digipymon(generar_digipymon_aleatorio())

    decision = input("¿Quieres combatir? (s/n): ")

    if decision.lower() != "s":
        print("Has huido y pierdes 1 digicoin.")
        jugador.digicoins = max(0, jugador.digicoins - 1)
        return

    victorias = 0
    derrotas = 0

    for i in range(jugador.cantidad_digipymon):

        tu_digipymon = jugador.lista_digipymon[i]
        enemigo_digipymon = enemigo.lista_digipymon[i]

        print("\nCombate:", tu_digipymon.nombre, "vs", enemigo_digipymon.nombre)

        if tu_digipymon.vida == 0:
            print("Tu digipymon está debilitado.")
            derrotas += 1
            continue

        if tu_digipymon.ataque > enemigo_digipymon.ataque:

            print("Ganas el combate.")
            victorias += 1

            tu_digipymon.vida -= enemigo_digipymon.ataque

        else:

            print("Pierdes el combate.")
            derrotas += 1

            diferencia = enemigo_digipymon.ataque - tu_digipymon.ataque
            tu_digipymon.vida -= diferencia

        if tu_digipymon.vida <= 0:
            tu_digipymon.vida = 0
            print(tu_digipymon.nombre, "se ha debilitado.")

    print("\nResultado final")

    if victorias > derrotas:
        print("Has ganado la batalla.")
        jugador.digicoins += victorias

    elif derrotas > victorias:
        print("Has perdido la batalla.")
        jugador.digicoins = max(0, jugador.digicoins - derrotas)

    else:
        print("Empate.")


def digishop(jugador, inventario):
    """
    Muestra la tienda y permite comprar objetos.

    Parameters
    ----------
    jugador : Jugador
        Jugador que compra.
    inventario : Inventario
        Inventario del jugador.
    """
    print("\n--- DIGISHOP ---")
    print("1. Digipyball (5 digicoins)")
    print("2. Pocion (3 digicoins)")
    print("3. Anabolizante (4 digicoins)")
    print("4. Salir")

    opcion = input("¿Qué quieres comprar?: ")

    if opcion == "1":
        if jugador.digicoins >= 5:
            inventario.añadir_objeto("digipyball", 1)
            jugador.digicoins -= 5
            print("Has comprado una digipyball.")
        else:
            print("No tienes suficientes digicoins.")

    elif opcion == "2":
        if jugador.digicoins >= 3:
            inventario.añadir_objeto("pocion", 1)
            jugador.digicoins -= 3
            print("Has comprado una poción.")
        else:
            print("No tienes suficientes digicoins.")

    elif opcion == "3":
        if jugador.digicoins >= 4:
            inventario.añadir_objeto("anabolizante", 1)
            jugador.digicoins -= 4
            print("Has comprado un anabolizante.")
        else:
            print("No tienes suficientes digicoins.")


def usar_item(jugador, inventario):
    """
    Permite al jugador usar un objeto del inventario sobre un Digipymon.

    Parameters
    ----------
    jugador : Jugador
        Jugador que usa el objeto.
    inventario : Inventario
        Inventario del jugador.
    """
    print("\n--- INVENTARIO ---")

    for objeto in inventario.objetos:
        print(objeto, ":", inventario.objetos[objeto])

    item = input("¿Qué objeto quieres usar?: ")

    if item not in inventario.objetos:
        print("No tienes ese objeto.")
        return

    if item == "digipyball":
        print("Las digipyballs no se pueden usar directamente.")
        return

    print("\nTus Digipymon:")
    for i in range(jugador.cantidad_digipymon):
        print(i, "-", jugador.lista_digipymon[i].nombre)

    indice = int(input("¿A qué Digipymon quieres usarlo?: "))

    digipymon = jugador.lista_digipymon[indice]

    if item == "pocion":
        digipymon.vida += 10
        print("La vida ha aumentado.")

    elif item == "anabolizante":
        digipymon.ataque += 5
        print("El ataque ha aumentado.")

    inventario.usar_objeto(item)


def main():
    """
    Función principal del juego. Inicia la aventura y gestiona el bucle del menú.
    """
    print("================================")
    print("      BIENVENIDO A DIGIPYMON")
    print("================================")

    nombre = input("Introduce tu nombre de entrenador: ")

    jugador = Jugador(nombre)
    inventario = Inventario()

    print("\nComienzas tu aventura en el mundo Digipymon.")

    primer_digipymon = generar_digipymon_aleatorio()
    jugador.añadir_digipymon(primer_digipymon)

    print("El profesor te ha regalado tu primer Digipymon:")
    print(primer_digipymon)

    inventario.añadir_objeto("digipyball", 3)
    inventario.añadir_objeto("pocion", 1)

    print("\nTambién recibes 3 digipyballs y una poción para empezar tu aventura.")

    while True:

        opcion = menu()

        if opcion == "1":
            buscar_digipymon(jugador, inventario)

        elif opcion == "2":
            combate(jugador)

        elif opcion == "3":
            digishop(jugador, inventario)

        elif opcion == "4":
            usar_item(jugador, inventario)

        elif opcion == "5":
            print(inventario.objetos)

        elif opcion == "6":
            jugador.consultar_digipymon()

        elif opcion == "7":
            print("Gracias por jugar.")
            break

        else:
            print("Opción inválida.")


main()