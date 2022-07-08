import requests
from django.contrib import messages
from math import acos, cos, sin, radians


def testConnect(request):
    try:
        connect = requests.get("www.google.com", timeout=5)
    except (requests.ConnectionError, requests.Timeout):
        print("Sin conexión a internet.")
        return messages.error(request, 'No tienes conexión a internet :(')
    else:
        print("Con conexión a internet.")



def distancia_puntos(punto_1, punto_2):
    punto_1 = (radians(punto_1[0]), radians(punto_1[1]))
    punto_2 = (radians(punto_2[0]), radians(punto_2[1]))

    distancia = acos(sin(punto_1[0])*sin(punto_2[0]) + cos(punto_1[0])*cos(punto_2[0])*cos(punto_1[1] - punto_2[1]))
    return distancia * 6371.01

def costo_envio(municipio):

    if municipio == 'ARROYO_NARANJO':
        envio = 5000
        return envio
    elif municipio == '10_DE_OCTUBRE':
        envio = 7500
        return envio
    elif municipio == 'CERRO':
        envio = 10000
        return envio
    elif municipio == 'LISA':
        envio = 12500
        return envio
    else:
        envio = 2000
        return envio


