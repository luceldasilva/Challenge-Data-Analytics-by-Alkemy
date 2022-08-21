# Descargar archivos .csv
from decouple import config
from datetime import datetime
from os import makedirs
from os import chdir
import requests as req

casa = config('my_base')
now = datetime.now()
mes = now.strftime('%Y-%B')
today = now.strftime('%d-%m-%Y')


with req.get('https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv') as rq:
    makedirs('museos//' + str(mes), exist_ok=True)
    chdir('museos//' + str(mes))
    with open('museos-' + str(today) + '.csv', 'wb') as file:
        file.write(rq.content)

with req.get('https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv') as rq:
    chdir(str(casa)) # Para volver al repertorio base y hacer las nuevas carpetas ahí
    makedirs('cine//' + str(mes), exist_ok=True)
    chdir('cine//' + str(mes))
    with open('cine-' + str(today) + '.csv', 'wb') as file:
        file.write(rq.content)

with req.get('https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv') as rq:
    chdir(str(casa))
    makedirs('biblioteca//' + str(mes), exist_ok=True)
    chdir('biblioteca//' + str(mes))
    with open('biblioteca-' + str(today) + '.csv', 'wb') as file:
        file.write(rq.content)
