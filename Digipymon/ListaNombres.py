import random

class ListaNombres:
    """
    Contiene listas de nombres para Digipymons y entrenadores.
    """

    def __init__(self):
        """
        Inicializa las listas de nombres disponibles.
        """
        self.lista_nombres_digipymons = [
            "Pyrodon", "Aquafy", "Terranox", "Voltiger", "Florania",
            "Sombrion", "Luminex", "Dracoryx", "Cryonix", "Toxikit",
            "Rocanid", "Electryx", "Nebulon", "Magmator", "Hydrantis",
            "Silphor", "Gravion", "Zephyros", "Ignistar", "Froston"
        ]

        self.lista_nombres_entrenadores = [
            "Carlos", "Lucía", "Miguel", "Sofía", "Andrés",
            "Valeria", "Javier", "Camila", "Diego", "Elena",
            "Raúl", "Martina", "Hugo", "Paula", "Iván",
            "Natalia", "Sergio", "Clara", "Adrián", "Laura"
        ]

    def obtener_nombre_digipymon(self):
        """
        Devuelve un nombre aleatorio para un Digipymon.

        Returns
        -------
        str
            Nombre aleatorio.
        """
        return random.choice(self.lista_nombres_digipymons)

    def obtener_nombre_entrenador(self):
        """
        Devuelve un nombre aleatorio para un entrenador.

        Returns
        -------
        str
            Nombre aleatorio.
        """
        return random.choice(self.lista_nombres_entrenadores)