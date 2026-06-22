#Sitema De Gestion De Paises

## Descripcion:
Este programa permite gestionar informacion de distintos paises mediante una interfaz de consola desarrollada en Python.
Los datos se cargan desde un archivo CSV y se almacenan en una lista de diccionarios. El usuario puede consultar, agregar, modificar, buscar, filtrar y ordenar paises segun distintos criterios.

## Funcionalidades:
- Mostrar todos los paises cargados.
- Agregar un nuevo pais.
- Actualizar datos de un pais existente.
- Buscar paises por nombre.
- Filtrar paises por continente.
- Filtrar paises por rango de poblacion.
- Filtrar paises por rango de superficie.
- Ordenar paises por nombre.
- Ordenar paises por población.
- Ordenar paises por superficie.
- Mostrar estadisticas generales.

## Requisitos:
Python 3.10 o superior.

## Archivos necesarios:
- main.py
- funciones.py
- datos.csv

## Ejecucion:
Abrir una terminal en la carpeta del proyecto y ejecutar:

python main.py

## A continuacion se mostrara el menu principal:
=== Sistema de Paises ===

1. Mostrar Pais
2. Agregar Pais
3. Actualizar Pais
4. Buscar Pais
5. Filtrar Continente
6. Filtrar Poblacion
7. Filtrar Superficie
8. Ordenar Nombre
9. Ordenar Poblacion
10. Ordenar Superficie
11. Estadisticas
0. Salir

Seleccione una opción ingresando el numero correspondiente.

## Ejemplos de uso:
Ejemplo 1: Agregar pais

Entrada

Nombre: Chile
Población: 19603733
Superficie: 756102
Continente: America

Salida

País agregado correctamente.

Ejemplo 2: Buscar pais

Entrada

Ingrese nombre del pais: argentina

Salida

País encontrado:

Nombre: Argentina
Población: 45376763
Superficie: 2780400
Continente: America

Ejemplo 3: Filtrar por continente

Entrada

Ingrese continente: America

Salida

Argentina - 45376763 habitantes
Brasil - 213993437 habitantes

Ejemplo 4: Estadisticas

Salida

=== ESTADÍSTICAS ===

Mayor población: Brasil (213993437)
Menor población: Argentina (45376763)

Promedio poblacion: 117829875.00
Promedio superficie: 2882791.00

Paises por continente:

America: 2
Asia: 1
Europa: 1

## Participación de los integrantes:

Integrantes:	Participación

Santiago Accastello:	Desarrollo de funciones de carga y validacion de datos
Fernado Guevara:	Implementación de búsquedas, filtros y ordenamientos
Santiago Accastello: Implementación de carga de datos desde CSV
Fernando Guevara:	Desarrollo de estadisticas
Santiago Accastello, Fernando Guevara: Desarrollo del menu principal
Santiago Accastello, Fernando Guevara:	Documentacion y pruebas del sistema


## Observaciones:
- Los datos se almacenan en un archivo CSV.
- Las validaciones evitan el ingreso de informacion incorrecta.
- El sistema funciona completamente desde la consola.


## Video Explicativo y Documento PDF:
- https://youtu.be/gkuWOxEv3VU
- https://1drv.ms/b/c/D3FA0AC68B6C8C85/IQAsijYU8-a-Qo1mQSQp44cCATeChblQfAOPFrLNzNgHJO4?e=YMt5sj
