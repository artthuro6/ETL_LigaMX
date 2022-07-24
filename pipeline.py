import pandas as pd 
import numpy as np
import ETL
import logging
import subprocess

from ETL.extract import Extract
#from transform import Transform
#from load import Load

logging.basicConfig( filename='log.txt', filemode='a',
                     format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                     level=logging.INFO, datefmt='%H:%M:%S')

def pipeline():
    """
    Funcion para invocar el ETL
    """
    #Recibiendo los datos de las paginas web
    logging.info(' Provando el requests a las paginas ')
    data_web = Extract()
    logging.info(data_web[1].status_code)
    logging.info(data_web[0].status_code)
    logging.info(' Requests exitoso. ')


    #Transformando los datos
    #transform_data = Transform( data_web )

    #Cargando los datos.
    #Load( transform_data )

    """Pendiente crear los logs diarios"""
    #subprocess.run([ 'mv', 'log.txt', './LOG'  ])


if __name__ == "__main__":
    pipeline()
