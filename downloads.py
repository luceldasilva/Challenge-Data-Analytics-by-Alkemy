# Descargar archivos .csv
from decouple import config
from datetime import datetime
import logging
import os
from os.path import isdir
from shutil import rmtree
import pyprojroot
import requests as req

now = datetime.now()
mes = now.strftime('%Y-%B')
today = now.strftime('%d-%m-%Y')


logging.basicConfig(
    format = '%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s', 
    level=logging.DEBUG, 
    filename='alkemy.log',  
    encoding="utf-8"
    )


def create_data():
    """
    Crear carpeta raíz del proyecto
    """
    if not isdir('data'):
        logging.error('No existe la carpeta ./data/')
        os.mkdir('data')
        logging.info('Carpeta creada')
    else:
        logging.info('La carpeta está disponible')


def downloads(file_link, art_venue):
    """
    Descargar los archivos fuentes
    """
    logging.info(f'Descargando {art_venue}')
    data_dir = pyprojroot.here('data')
    os.chdir(str(data_dir))
    with req.get(str(file_link)) as rq:
        if isdir(str(art_venue)):
            rmtree(str(art_venue))
        os.makedirs(os.path.join(data_dir, str(art_venue), str(mes)))
        os.chdir(os.path.join(data_dir, str(art_venue), str(mes)))
        with open(f'{str(art_venue)}-{str(today)}.csv', 'wb') as file:
            file.write(rq.content)
            logging.info(f'categoría {art_venue} descargada')


def run():
    create_data()
    downloads(config('museo_link'), 'museos')
    downloads(config('cine_link'), 'cine')
    downloads(config('biblioteca_link'), 'biblioteca')

if __name__ == '__main__':
    run()