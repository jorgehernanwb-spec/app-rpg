
class inventario:
    def __init__(self):
        self.objetos = []

    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)
        print("Objeto agregado correctamente")

    def mostrar_inventario(self):
        if len(self.objetos) == 0:
            print("El inventario está vacío")
        else:
            print("Objetos del inventario:")

            for objeto in self.objetos:
                print(objeto)
