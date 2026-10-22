
class objeto:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Tipo:", self.tipo)
