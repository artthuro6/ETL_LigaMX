import pandas as pd 
import numpy as np 
import os 
import requests

#Urls de acceso
url_1 = 'https://www.tudn.com/futbol/liga-mx/resultados'
url_2 = 'https://www.tudn.com/futbol/liga-mx/posiciones'

#Funcion principal
def Extract():
    """
    Obtencion de los datos
    """

    return ( _acces_to_page(url_1, url_2) )
    


def _acces_to_page(url_1, url_2):
    x1 = requests.get(url_1)
    x2 = requests.get(url_2)

    return (x1, x2)


