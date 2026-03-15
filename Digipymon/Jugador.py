class Jugador:
    """
    Representa al jugador principal, que posee Digipymons y digicoins.
    """

    def __init__(self, nombre):
        """
        Inicializa un nuevo jugador.

        Parameters
        ----------
        nombre : str
            Nombre del jugador.
        """
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        self.digicoins = 10

    def añadir_digipymon(self, digipymon):
        """
        Añade un Digipymon al equipo del jugador.

        Parameters
        ----------
        digipymon : Digipymon
            Digipymon que se añadirá al equipo.
        """
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon += 1

    def consultar_digipymon(self):
        """
        Muestra por pantalla todos los Digipymons del jugador.
        """
        for digipymon in self.lista_digipymon:
            print(digipymon)

    def consultar_digicoins(self):
        """
        Muestra la cantidad actual de digicoins del jugador.
        """
        print(self.digicoins)