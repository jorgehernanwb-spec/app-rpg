
class jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.personaje = None

    def seleccionar_personaje(self, personaje):
        self.personaje = personaje
        print("Personaje seleccionado correctamente")

    def mostrar_personaje(self):
        if self.personaje is not None:
            print("Jugador:", self.nombre)
            print("Personaje:", self.personaje.nombre)
        else:
            print("No has seleccionado un personaje")
