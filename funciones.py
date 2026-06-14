import csv

#Menu
def mostrar_menu():

    print('=== Sistema de Paises ===\n')
    print('1. Mostrar Pais')
    print('2. Agregar Pais')
    print('3. Actualizar Pais')
    print('0. Salir')
    

#Cargar Datos
def cargar_paises(nombre_archivo):
    """Lee el archivo CSV y devuelve una lista de paises"""
    paises = []

    try:
        with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            columnas_esperadas = {"nombre", "poblacion", "superficie", "continente"}

            if set(lector.fieldnames) != columnas_esperadas:
                raise ValueError("El CSV tiene columnas incorrectas.")

            for fila in lector:
                try:
                    pais = {"nombre": fila["nombre"].strip(), "poblacion": int(fila["poblacion"]), "superficie": int(fila["superficie"]), "continente": fila["continente"].strip()}

                    paises.append(pais)

                except ValueError:
                    print(f"Registro invalido omitido: {fila}")

    except FileNotFoundError:
        print("No se encontro el archivo CSV.")
    except Exception as error:
        print(f"Error al cargar archivo: {error}")

    return paises


#Validaciones
#Solicita un texto al usuario y verifica que no esté vacío. Si el usuario no escribe nada, vuelve a pedir el dato
def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()

        if valor:
            return valor

        print("Error: no puede quedar vacio")

#Solicita un número entero positivo valida que sea un numero y sea mayor a cero
def pedir_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))

            if valor > 0:
                return valor

            print("Debe ser mayor que cero")

        except ValueError:
            print("Ingrese un numero valido")

#solicita al usuario que ingrese un continente y verifica que el valor corresponda a uno de los cinco continentes permitidos
def pedir_continente():
    continentes_validos = ["América", "Europa", "Asia", "África", "Oceanía"]

    while True:
        continente = input("Continente: ").strip().capitalize()

        if continente in continentes_validos:
            return continente

        print("Error: debe ingresar uno de estos continentes:")
        print(", ".join(continentes_validos))


#Mostrar Paises
#Muestra en pantalla todos los paises almacenados en la lista paises = []
def mostrar_paises(paises):

    if not paises:
        print("\nNo hay paises para mostrar.")
        return

    print("\n" + "-" * 80)

    for pais in paises:
        print( f"{pais['nombre']:<15}" f"Poblacion: {pais['poblacion']:<12}" f"Superficie: {pais['superficie']:<12}" f"Continente: {pais['continente']}")

    print("-" * 80)


#Agregar Pais
#Permite ingresar un nuevo pais al sistema
def agregar_pais(paises):
    nombre = pedir_texto("Nombre: ").strip().capitalize()

    existe = any(pais["nombre"].lower() == nombre.lower() for pais in paises)

    if existe:
        print("Ese pais ya existe.")
        return

    poblacion = pedir_entero_positivo("Poblacion: ")
    superficie = pedir_entero_positivo("Superficie: ")
    continente = pedir_continente()

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)

    print("Pais agregado correctamente.")



#Actualizar Pais
#Permite modificar los datos de un pais ya existente
def actualizar_pais(paises):
    nombre = pedir_texto(
        "Ingrese el nombre del pais a actualizar: "
    )

    for pais in paises:

        if pais["nombre"].lower() == nombre.lower():

            pais["poblacion"] = pedir_entero_positivo("Nueva poblacion: ")

            pais["superficie"] = pedir_entero_positivo("Nueva superficie: ")

            print("Datos actualizados")
            return

    print("Pais no encontrado.")


# Buscar pais
# Permite buscar un pais dentro de la lista
def buscar_pais(paises):


    if not paises:
        print("No hay países cargados.")
        return

    busqueda = input("Ingrese nombre del país: ").strip().lower()

    encontrado = False

    for pais in paises:

        if busqueda in pais["nombre"].lower():

            print("\nPaís encontrado:")
            print(f"Nombre: {pais['nombre']}")
            print(f"Población: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']}")
            print(f"Continente: {pais['continente']}")

            encontrado = True

    if not encontrado:
        print("No se encontraron coincidencias.")

# Filtrar por Continente
# Muestra los países pertenecientes a un continente
def filtrar_continente(paises):

    continente = input(
        "Ingrese continente: "
    ).strip().capitalize()

    encontrados = False

    for pais in paises:

        if pais["continente"] == continente:

            print(
                f"{pais['nombre']} - "
                f"{pais['poblacion']} habitantes"
            )

            encontrados = True

    if not encontrados:
        print("No hay resultados.")