class Enemigo:
    """
    Representa a un entrenador enemigo con su propio equipo de Digipymons.
    """

    def __init__(self, nombre):
        """
        Inicializa un nuevo enemigo.

        Parameters
        ----------
        nombre : str
            Nombre del entrenador enemigo.
        """
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0

    def añadir_digipymon(self, digipymon):
        """
        Añade un Digipymon al equipo del enemigo.

        Parameters
        ----------
        digipymon : Digipymon
            Digipymon que se añadirá al equipo.
        """
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon += 1