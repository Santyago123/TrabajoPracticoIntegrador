from funciones import *

#Programa Principal
def main():

    paises = cargar_paises("datos.csv")

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: \n")

        match opcion:

            case "1":
                mostrar_paises(paises)

            case "2":
                agregar_pais(paises)

            case "3":
                actualizar_pais(paises)

            case "0":
                print("Programa finalizado.")
                break

            case _:
                print("Opción inválida.")

#Esto indica cual es el punto de inicio del programa
if __name__ == "__main__":
    main()
