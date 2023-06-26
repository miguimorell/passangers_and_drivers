# TFM


import urllib
import requests
import mysql.connector
from API import *
from GeneradorDistancias import *

# SQL
import sqlite3

"""tabla = '''CREATE TABLE PASAJEROS(
    NOMBRE CHAR(20) NOT NULL,
    ORIGEN CHAR(40) NOT NULL,
    DESTINO CHAR(40) NOT NULL
    )'''"""
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()
#cursor.execute("DROP TABLE IF EXISTS PASAJEROS")
#cursor.execute(tabla)

# Función que inserta los datos en la base de datos de un pasajero
def insertar_datos_pasajero(nombre, origen, destino):
    datos = [nombre, origen, destino]
    print(f"Se va a insertar lo siguiente:{datos}")
    cursor.execute(
        "INSERT INTO PASAJEROS (NOMBRE, ORIGEN, DESTINO) VALUES ('{}', '{}', '{}')".format(datos[0], datos[1],
                                                                                           datos[2]))
    return


# Función que proporciona las direcciones de todos los posibles pasajeros
def proporcionar_direcciones_():
    cursor.execute("SELECT * FROM PASAJEROS")
    items = cursor.fetchall()
    origenes = []
    destinos = []

    for item in items:
        origenes.append(item[1])
        destinos.append(item[2])
    print(origenes)
    return origenes, destinos


# Variables Inicializar
viajar_ahora = False
procedencia_no_valida = True
conductor_o_pasajero = True
origen_api = ""
vectordistanciasprueba = []
direccion_correcta = 1

# Menú iniciar viaje
while not viajar_ahora:  # El bucle while se repetirá hasta que el usuario decida que quiere viajar.
    respuesta_deseo_viajar = input("¿Desea realizar un trayecto ahora? \n(Presione 'y' para sí 'n' para no) \n ")
    if respuesta_deseo_viajar == "y" or respuesta_deseo_viajar == "Y":
        viajar_ahora = True
        print("¡De acuerdo! ¡Vamos a viajar!")
        usuario = {}  # Inicializar/vaciar diccionario usuario
    elif respuesta_deseo_viajar == "n" or respuesta_deseo_viajar == "N":
        viajar_ahora = False
        print("¡De acuerdo! ¡Hasta pronto!")
    else:
        print("Ha introducido una respuesta errónea")

# Menu: Nombre y apellidos
nombre = str(
    input("Introduzca su nombre y apellidos \n"))
usuario["Nombre"] = nombre

# Menu conductor vs pasajero
while conductor_o_pasajero:  # El bucle se repetirá hasta que se indique que se seleccione conductor o pasajero.
    respuesta_conductor_o_pasajero = input(
        "¿Desea realizar el viaje como conductor o como pasajero? \n(Presione 'c' para "
        "conductor, 'p' para pasajero) \n ")

    if respuesta_conductor_o_pasajero == "c" or respuesta_conductor_o_pasajero == "C":
        #######################################
        print("¡De acuerdo! ¡Vamos a buscar pasajeros!")
        conductor_o_pasajero = False  # Variable para salir del bucle while
        conduce = True  # Variable para almacenar si es conductor o pasajero
        usuario["Conduce"] = conduce

    elif respuesta_conductor_o_pasajero == "p" or respuesta_conductor_o_pasajero == "P":
        print("¡De acuerdo! ¡Vamos a buscar conductores!")
        conductor_o_pasajero = False  # Variable para salir del bucle while
        conduce = False  # Variable para almacenar si es conductor o pasajero
        usuario["Conduce"] = conduce
    else:
        print("Ha introducido una respuesta errónea")

# Menu: Procedencia
while procedencia_no_valida:  # Se continuará preguntando la ubicación de origen hasta obtener una respuesta válida
    respuesta_origen = input("¿Desde dónde comenzará su viaje? \n(Presione 'g' para Getafe, 'i' para Illescas o 'o' "
                             "para usar otra \n")
    print(respuesta_origen)
    if respuesta_origen == "g" or respuesta_origen == "G":
        origen_api = "P.º John Lennon, s/n, 28906 Getafe, Madrid"  # Variable para almacenar la dirección de envio a la API
        usuario["Origen"] = origen_api
        procedencia_no_valida = False
    elif respuesta_origen == "i" or respuesta_origen == "I":
        origen_api = "C. Sierra de Gredos, 7, 45200 Illescas, Toledo, Spain"
        usuario["Origen"] = origen_api
        procedencia_no_valida = False
    elif respuesta_origen == "o" or respuesta_origen == "O":
        while direccion_correcta != 0:
            origen_api = input(
                "Introduzca la dirección desde donde desea realizar el viaje siguiendo el siguiente modelo: "
                "\n['CALLE', 'NUMERO', 'CÓDIGO POSTAL', 'POBLACIÓN', 'CIUDAD', 'PAÍS'] \n")  # SI SE PONE UNA DIRECCION ERRONEA? duda 3
            usuario["Origen"] = origen_api
            respuesta_API = API(usuario["Origen"],
                                "P.º John Lennon, s/n, 28906 Getafe, Madrid")  # comprueba que la dirección introducida es válida
            direccion_correcta = respuesta_API[0]
            if direccion_correcta != 0:
                print(f"Dirección introducida errónea, por favor, introduzca una dirección válida")
            procedencia_no_valida = False

# Menu: Destino
destino_correcto = 1
while destino_correcto != 0:
    destino_api = input("Introduzca la dirección de destino siguiendo el siguiente modelo: "
                        "\n['CALLE', 'NUMERO', 'CÓDIGO POSTAL', 'POBLACIÓN', 'CIUDAD', 'PAÍS'] \n")
    usuario["Destino"] = destino_api
    respuesta_API = API(usuario["Destino"],
                        "P.º John Lennon, s/n, 28906 Getafe, Madrid")  # comprueba que la dirección introducida es válida
    destino_correcto = respuesta_API[0]
    if destino_correcto != 0:
        print(f"Dirección errónea, por favor, introduzca una dirección válida \n")

print(usuario)
if not usuario["Conduce"]:  # Si la variable conduce es False, es decir si es un pasajero...:
    # INSERTAR DATOS EN SQL

    print("Se ha creado la tabla 'PASAJEROS'")
    insertar_datos_pasajero(usuario["Nombre"], usuario["Origen"], usuario["Destino"])

elif usuario["Conduce"]:  # Si la variable conduce es True, es decir si es un conductor...:
    # 1) Consultar la base de datos SQL para ver los origenes/destiones de los pasajeros actuales
    origenes_pasajeros, destinos_pasajeros = proporcionar_direcciones_()
    distancias_con_pasajeros_origenes = []
    distancias_con_pasajeros_destinos = []
    # 2)Enviar a la API los el origen/destino del conductor y compararlo con los de los pasajeros
    for i in range(len(origenes_pasajeros)):
        distancias_con_pasajeros_origenes.append(API(usuario["Origen"], origenes_pasajeros[i]))
        distancias_con_pasajeros_destinos.append(API(usuario["Destino"], destinos_pasajeros[i]))

    # )enviar las distancias obtenidas
    eleccion = calculadora_minimas_distancias(distancias_con_pasajeros_origenes, distancias_con_pasajeros_destinos)

    print(f"Se ha escogido al conductor número {eleccion}, se procede a contactar con el. ¡Buen viaje!\n")

# Commit our command
conn.commit()

# Close our connection
conn.close()
