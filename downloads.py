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
    if isdir('data') == False:
        os.mkdir('data')
        logging.info('carpeta creada')
    else:
        logging.info('carpeta disponible')


def downloads(file_link, art_venue):
    logging.info(f'Descargando {art_venue}')
    CURRENT_DIR = pyprojroot.here('data')
    os.chdir(str(CURRENT_DIR))
    with req.get(str(file_link)) as rq:
        if isdir(str(art_venue)) == True:
            rmtree(str(art_venue))
        os.makedirs(os.path.join(CURRENT_DIR, str(art_venue), str(mes)))
        os.chdir(os.path.join(CURRENT_DIR, str(art_venue), str(mes)))
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