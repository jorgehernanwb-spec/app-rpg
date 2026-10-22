from personaje import personaje

class mago(personaje):
    def __init__(self, nombre, nivel, vida, poder_magico):
        super().__init__(nombre, nivel, vida)
        self.poder_magico = poder_magico

    def atacar(self):
        print(self.nombre, "lanza un ataque mágico")

    def usar_habilidad(self):
        print(self.nombre, "utiliza un hechizo")
        print("Poder mágico:", self.poder_magico)
