
from jugador import jugador
from mago import mago
from guerrero import guerrero
from objeto import objeto

print("=== BIENVENIDO AL RPG ===")

nombre = input("Ingresa tu nombre: ")
jugador1 = jugador(nombre)

print("\nSelecciona un personaje:")
print("1. Mago")
print("2. Guerrero")

opcion = input("Elige una opción: ")

if opcion == "1":
    personaje1 = mago("merlin", 1, 100, 50)

elif opcion == "2":
    personaje1 = guerrero("arturo", 1, 100, 40)

else:
    print("Opción no válida")
    personaje1 = None

if personaje1 is not None:

    jugador1.seleccionar_personaje(personaje1)

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Mostrar personaje")
        print("2. Atacar")
        print("3. Usar habilidad")
        print("4. Recibir daño")
        print("5. Agregar objeto")
        print("6. Mostrar inventario")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            personaje1.mostrar_informacion()

        elif opcion == "2":
            personaje1.atacar()

        elif opcion == "3":
            personaje1.usar_habilidad()

        elif opcion == "4":
            cantidad = 20
            personaje1.recibir_danio(cantidad)

        elif opcion == "5":
            nombre_objeto = input("Nombre del objeto: ")
            tipo_objeto = input("Tipo de objeto: ")

            objeto1 = objeto(nombre_objeto, tipo_objeto)
            personaje1.inventario.agregar_objeto(objeto1)

        elif opcion == "6":
            if len(personaje1.inventario.objetos) == 0:
                print("El inventario está vacío")
            else:
                for item in personaje1.inventario.objetos:
                    item.mostrar_informacion()

        elif opcion == "7":
            print("Gracias por jugar")
            break

        else:
            print("Opción no válida")
