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

            case "4":
                buscar_pais(paises)

            case "5":
                filtrar_continente(paises)

            case "6":
                filtrar_poblacion(paises)

            case "7":
                filtrar_superficie(paises)

            case "8":
                ordenar_nombre(paises)

            case "9":
                ordenar_poblacion(paises)

            case "10":
                ordenar_superficie(paises)

            case "11":
                estadisticas(paises)

            case "0":
                print("Programa finalizado.")
                break

            case _:
                print("Opción inválida.")

#Esto indica cual es el punto de inicio del programa
if __name__ == "__main__":
    main()
