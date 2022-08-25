# Descargar archivos .csv
from decouple import config
from datetime import datetime
import logging
from os import makedirs
from os import chdir
import requests as req

casa = config('my_base') #configurar directorio actual en .env
now = datetime.now()
mes = now.strftime('%Y-%B')
today = now.strftime('%d-%m-%Y')


logging.basicConfig(
    format = '%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s', 
    level=logging.DEBUG, 
    filename='alkemy.log',  
    encoding="utf-8"
    )


def downloads(file_link, art_venue):
    with req.get(str(file_link)) as rq:
        chdir(str(casa))
        makedirs(f'{str(art_venue)}//{str(mes)}', exist_ok=True)
        chdir(f'{str(art_venue)}//{mes}')
        with open(f'{str(art_venue)}-{str(today)}.csv', 'wb') as file:
            file.write(rq.content)
            logging.info(f'categoría {art_venue} descargada')


logging.info('Descargando archivos')


def run():
    downloads(config('museo_link'), 'museos')
    downloads(config('cine_link'), 'cine')
    downloads(config('biblioteca_link'), 'biblioteca')

if __name__ == '__main__':
    run()