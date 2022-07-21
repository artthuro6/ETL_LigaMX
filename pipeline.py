import pandas as pd 
import numpy as np
import logging
logging.basicConfig(level=logging.INFO)

from extract import Extract
#from transform import Transform
#from load import Load

def pipeline():
    """
    Funcion para invocar el ETL
    """
    
    #Recibiendo los datos de las paginas web
    data_web = Extract()
    logging.info(data_web[1].status_code)
    logging.info(data_web[0].status_code)
    

    #Transformando los datos
    #transform_data = Transform( data_web )

    #Cargando los datos.
    #Load( transform_data )

    


if __name__ == "__main__":
    pipeline()