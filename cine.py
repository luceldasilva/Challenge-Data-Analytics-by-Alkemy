# from os.path import abspath
# from os.path import isdir
from pathlib import Path
import pyprojroot
# from decouple import config
import numpy as np
import pandas as pd
import logging

def cine():
    """
    Tabla exclusiva de cine para mostrar cantidades de pantallas, butacas y disponibilidad de espacios INCAA
    """
    logging.info('Creando tabla de cine')
    dir_cine = Path(str(pyprojroot.here('data').joinpath('cine'))).glob("**/*.csv")
    for buscar_cine in dir_cine:
        df_cine = pd.read_csv(buscar_cine, header = 0, sep = ',')
        df_cine.columns = df_cine.columns.str.lower()
        df_cine.espacio_incaa = df_cine.espacio_incaa.replace(['0'], np.nan)
        df_cine.espacio_incaa = df_cine.espacio_incaa.fillna('No')
        df_cine.espacio_incaa = df_cine.espacio_incaa.str.lower()
        df_cine = df_cine.replace(['Ciudad Autónoma de Buenos Aires'], ['Capital Federal'])
        df_cine.provincia = df_cine.provincia.str.strip()
        espacios = df_cine.groupby(['provincia'])['espacio_incaa'].apply(lambda x: x[x == 'si'].count()).reset_index(name='espacio_incaa').sort_values('provincia', ascending=1)    
        tablita = df_cine.groupby(['provincia']).aggregate({'pantallas':'sum','butacas':'sum'}).sort_values('provincia', ascending=1)
        tablita = tablita.merge(espacios, on='provincia')
        with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.precision', 3):
            print(tablita)
            logging.info('Tabla de cine impresa')

if __name__ == '__main__':
    cine()