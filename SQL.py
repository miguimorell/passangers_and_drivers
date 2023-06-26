import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('usuarios.db')
# Create a cursor object using cursor() method
cursor = conn.cursor()

# Doping PASAJEROS table if already exists:
cursor.execute("DROP TABLE IF EXISTS PASAJEROS")

# Creating table

tabla = '''CREATE TABLE PASAJEROS(
    NOMBRE CHAR(20) NOT NULL, 
    ORIGEN CHAR(40) NOT NULL,
    DESTINO CHAR(40) NOT NULL
    )'''
cursor.execute(tabla)
print("Se ha creado la tabla 'PASAJEROS'")


# Función que inserta los datos en la base de datos de un pasajero
def insertar_datos_pasajero(nombre, origen, destino):
    datos = [nombre, origen, destino]
    print(f"Se va a insertar lo siguiente:{datos}")
    cursor.execute("INSERT INTO PASAJEROS (NOMBRE, ORIGEN, DESTINO) VALUES ('{}', '{}', '{}')".format(datos[0], datos[1],datos[2]))
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


#insertar_datos_pasajero("miguel", "Paris", "Madrid")
#insertar_datos_pasajero("miguel", "Valencia", "Cuenca")
#insertar_datos_pasajero("miguel", "Albacete", "Torrelavega")
#insertar_datos_pasajero("miguel", "Amsterdam", "Berlin")
origenes_p,destinos_p=proporcionar_direcciones_()
#print(f"Origenes pasajeros:{origenes_p}")
#print(f"Destinos pasajeros:{destinos_p}")

# Commit our command
conn.commit()

# Close our connection
conn.close()
