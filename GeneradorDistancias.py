import random


# def generador_distancias_aleatorio():
#    numero_pasajeros = (random.randint(5, 8))
#    distancias_origen = []
#    distancias_destino = []
#   dicc={}
#    for index in range(numero_pasajeros):
#        distancias_origen.append(random.randint(0, 50))
#        distancias_destino.append(random.randint(0, 50))

#   return distancias_origen, distancias_destino
# distancias_entre_origen, distancias_entre_destino = generador_distancias_aleatorio()
# print(distancias_entre_origen)
# print(distancias_entre_destino)
# distancia_total_desvio = []


def calculadora_minimas_distancias(distancias_entre_origen, distancias_entre_destino):
    # distancias_entre_origen, distancias_entre_destino = generador_distancias_aleatorio()

    distancia_total_desvio = []
    out = True

    # calcula la distancia mínima entre el origen del conductor y el de todos los pasajeros
    minima_distancia_origen = min(distancias_entre_origen)
    # calcula la distancia mínima entre el destino del conductor y el de todos los pasajeros
    minima_distancia_destino = min(distancias_entre_destino)
    # Encuentra la posición en el vector distancias de la menor distancia entre origenes:
    minima_distancia_origen_position = distancias_entre_origen.index(min(distancias_entre_origen))
    # Encuentra la posición en el vector distancias de la menor distancia entre destinos:
    minima_distancia_destino_position = distancias_entre_destino.index(min(distancias_entre_destino))


    # Calcula la distancia total de desviación como la suma de distancias de origen y destino:
    for index in range(len(distancias_entre_origen)):
        distancia_total_desvio.append([distancias_entre_origen[index] + distancias_entre_destino[index]])
    minima_distancia_total = min(distancia_total_desvio)
    minima_distancia_total_position = distancia_total_desvio.index(min(distancia_total_desvio))

    dicc_distancias = {minima_distancia_origen_position: minima_distancia_origen,
                       minima_distancia_destino_position: minima_distancia_destino,
                       minima_distancia_total_position: minima_distancia_total}
    print(f"La mínima distancia de recogida es:{round(minima_distancia_origen[1],2)}km, aproximadamente unos {minima_distancia_origen[2]} minutos")
    print(f"Se da con el pasajero número:{minima_distancia_origen_position}")

    print(f"La mínima distancia en la dejada es:{round(minima_distancia_destino[1],2)}Km, aproximadamente unos {minima_distancia_destino[2]} minutos")
    print(f"Se da con el pasajero número:{minima_distancia_destino_position}")

    print(f"La mínima distancia total de desvío es:{round(minima_distancia_total[0][4],2)}Km, aproximadamente unos {minima_distancia_total[0][5]} minutos")
    print(f"Se da con el conductor número:{minima_distancia_total_position}")



    while out:



        if minima_distancia_total_position != minima_distancia_origen_position != minima_distancia_destino_position:
            number = input(
                f"Elija el pasajero que desea recoger en base a estos datos. Escoja entre el número {minima_distancia_origen_position}, el número {minima_distancia_destino_position} ó el numero {minima_distancia_total_position}")
        elif minima_distancia_total_position == minima_distancia_origen_position:
            number = input(f"Elija el pasajero que desea recoger en base a estos datos. Escoja entre el número {minima_distancia_destino_position} ó el numero {minima_distancia_total_position}")
        else:
            number = input(
                f"Elija el pasajero que desea recoger en base a estos datos. Escoja entre el número {minima_distancia_origen_position} ó el numero {minima_distancia_total_position}")
        if number.isdigit() and int(number)==minima_distancia_total_position or int(number)==minima_distancia_origen_position or int(number) == minima_distancia_destino_position:

            out = False
        else:
            print("Respuesta errónea, introduzca un valor correcto")

    return number


