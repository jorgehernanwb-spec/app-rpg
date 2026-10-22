from personaje import personaje

class guerrero(personaje):
    def __init__(self, nombre, nivel, vida, fuerza):
        super().__init__(nombre, nivel, vida)
        self.fuerza = fuerza

    def atacar(self):
        print(self.nombre, "realiza un ataque con su espada")

    def usar_habilidad(self):
        print(self.nombre, "utiliza un golpe poderoso")
        print("Fuerza:", self.fuerza)
