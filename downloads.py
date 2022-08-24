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
    filemode='w', 
    encoding="utf-8"
    )

logging.info('Descargando archivos')

with req.get('https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv') as rq:
    makedirs(f'museos//{str(mes)}', exist_ok=True)
    chdir(f'museos//{mes}')
    with open(f'museos-{str(today)}.csv', 'wb') as file:
        file.write(rq.content)
        logging.info('categoría museo descargada')

with req.get('https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv') as rq:
    chdir(str(casa)) # Para volver al repertorio base y hacer las nuevas carpetas ahí
    makedirs(f'cine//{str(mes)}', exist_ok=True)
    chdir(f'cine//{str(mes)}')
    with open(f'cine-{str(today)}.csv', 'wb') as file:
        file.write(rq.content)
        logging.info('categoría cine descargada')


with req.get('https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv') as rq:
    chdir(str(casa))
    makedirs(f'biblioteca//{str(mes)}', exist_ok=True)
    chdir(f'biblioteca//{str(mes)}')
    with open(f'biblioteca-{str(today)}.csv', 'wb') as file:
        file.write(rq.content)
        logging.info('categoría biblioteca descargada')