from inventario import inventario
class personaje:
    def __init__(self, nombre, nivel, vida):
        self.nombre = nombre
        self.nivel = nivel
        self.vida = vida
        self.inventario = inventario()

    def atacar(self):
        print(self.nombre, "realiza un ataque")

    def recibir_danio(self, cantidad):
        self.vida -= cantidad
        print(self.nombre, "recibió", cantidad, "de daño")

    def usar_habilidad(self):
        print(self.nombre, "utiliza una habilidad")

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Nivel:", self.nivel)
        print("Vida:", self.vida)

