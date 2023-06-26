

def API(origen, destino):
    # API
    import urllib
    import requests
    api_url = "https://www.mapquestapi.com/directions/v2/route?"
    key_api = "mlcqr0F1gjH6jgEMjbbvjOd2reHRKsMU"
    origin_api = origen
    destination_api = destino
    url = api_url + urllib.parse.urlencode({"key": key_api, "from": origin_api, "to": destination_api})
    print(url)
    json_data = requests.get(url).json()
    #Status Code
    status_code=json_data["info"]["statuscode"]   #Comprobación de que funciona
    #Distancia
    try:
        distancia_miles=json_data["route"]["distance"]
    except:
        distancia_miles=0
    distancia_km=distancia_miles*1.60934
    #Tiempo
    try:
        tiempo=json_data["route"]["formattedTime"]
    except:
        tiempo=0

    return status_code, distancia_km, tiempo

