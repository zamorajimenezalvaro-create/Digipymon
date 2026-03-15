class Inventario:
    """
    Gestiona los objetos que posee el jugador.
    """

    def __init__(self):
        """
        Inicializa un inventario vacío.
        """
        self.objetos = {}

    def añadir_objeto(self, nombre, cantidad):
        """
        Añade una cantidad de un objeto al inventario.

        Parameters
        ----------
        nombre : str
            Nombre del objeto.
        cantidad : int
            Cantidad a añadir.
        """
        if nombre in self.objetos:
            self.objetos[nombre] += cantidad
        else:
            self.objetos[nombre] = cantidad

    def usar_objeto(self, nombre):
        """
        Usa un objeto del inventario, reduciendo su cantidad.

        Parameters
        ----------
        nombre : str
            Nombre del objeto a usar.
        """
        if nombre in self.objetos:
            self.objetos[nombre] -= 1

            if self.objetos[nombre] <= 0:
                del self.objetos[nombre]
        else:
            print("No tienes ese objeto")