from os import mkdir
import requests as req

with req.get('https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv') as rq:
    mkdir('museos')
    mkdir('C://Users//user//Documents//lucelprojects//challenge-alkemy//museos//2022-agosto')
    with open('C://Users//user//Documents//lucelprojects//challenge-alkemy//museos//2022-agosto//museos-19-08-2022.csv', 'wb') as file:
        file.write(rq.content)


with req.get('https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv') as rq:
    mkdir('cine')
    mkdir('C://Users//user//Documents//lucelprojects//challenge-alkemy//cine//2022-agosto')
    with open('C://Users//user//Documents//lucelprojects//challenge-alkemy//cine//2022-agosto//cine-19-08-2022.csv', 'wb') as file:
        file.write(rq.content)

with req.get('https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv') as rq:
    mkdir('biblioteca')
    mkdir('C://Users//user//Documents//lucelprojects//challenge-alkemy//biblioteca//2022-agosto')
    with open('C://Users//user//Documents//lucelprojects//challenge-alkemy//biblioteca//2022-agosto//biblioteca-19-08-2022.csv', 'wb') as file:
        file.write(rq.content)
