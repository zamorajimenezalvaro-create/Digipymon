class Digipymon:
    """
    Representa un Digipymon con atributos básicos como nombre, vida,
    ataque, tipo y nivel.
    """

    def __init__(self, nombre, vida, ataque, tipo, nivel):
        """
        Inicializa un nuevo Digipymon.

        Parameters
        ----------
        nombre : str
            Nombre del Digipymon.
        vida : int
            Puntos de vida iniciales.
        ataque : int
            Valor de ataque base.
        tipo : str
            Tipo elemental del Digipymon (fuego, agua, planta).
        nivel : int
            Nivel del Digipymon.
        """
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.tipo = tipo
        self.nivel = nivel

    def __str__(self):
        """
        Devuelve una representación en texto del Digipymon.

        Returns
        -------
        str
            Cadena con los atributos principales del Digipymon.
        """
        return (
            f"Nombre: {self.nombre}, "
            f"Vida: {self.vida}, "
            f"Ataque: {self.ataque}, "
            f"Tipo: {self.tipo}, "
            f"Nivel: {self.nivel}"
        )