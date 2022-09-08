# Challenge Data Analytics - Python

> Este es mi repositorio del challenge de Alkemy

## Objetivo 👈
Crear un proyecto que consuma datos desde 3 fuentes distintas para tener una base de datos SQL con información cultural sobre bibliotecas, museos y salas de cines argentinos.

## Estructura del Proyecto 📦

    ├── data           <- Carpeta raíz que almacene las descargas.
	│   ├── biblioteca
	│   │    ├── Mes de descarga
	│   │         └── biblioteca-día-de-la-descarga.csv
    │   ├── cine
	│   │    ├── Mes de descarga
	│   │         └── cine-día-de-la-descarga.csv
    │   ├── museos
	│       ├── Mes de descarga
	│            └── museos-día-de-la-descarga.csv
	│
	├── venv           <- Carpeta del ambiente virtual
    ├── .env     <- Archivo para la conexión de base de datos y descargas.
	├── .gitignore     <- Ignorar carpetas data que el programa creará y venv.
	├── alkemy.log             <- Archivo de registro que sucede en el código.
    ├── alkemy.py             <- La estrella del proyecto.
    ├── puntoenv.txt          <- Plantilla para crear el archivo .env
	├── README.md          <- La guía del proyecto.
    ├── requirements.txt            <- Librerías del proyecto
    ├── table_create.sql   <- Tabla inicial para manipular los datos en sql

## Proceso de Instalación ⚙️
![](https://thumbs.gfycat.com/UglyEminentEidolonhelvum-size_restricted.gif)

1. Clonar repositorio
``` bash
git clone https://github.com/luceldasilva/Challenge-Data-Analytics-by-Alkemy.git && cd Challenge-Data-Analytics-by-Alkemy
```
también se puede [descargar como archivo.zip aquí](https://github.com/luceldasilva/cookiecutter-personal/archive/refs/heads/main.zip "descargar en archivo.zip aquí") y descomprimirlo.

2. Crear ambiente virtual para ejecutar el programa
En Windows
``` bash
py -m venv venv && venv\Scripts\activate
```
En Linux y Mac
``` bash
python3 -m venv venv && source venv/bin/activate
```

3. Instalar las librerías contenidas en requirements.txt
``` bash
pip install -r requirements.txt
```

4. Crear archivo .env copiando del archivo puntoenv.txt
> Reemplazar por el password correspondiente de su usuario
![Imgur](https://i.imgur.com/4jExZDY.png)

Todo Listo ya se podrá ejecutar el alkemy.py en tu directorio
En Windows
``` bash
py alkemy.py
```
En Linux y Mac
``` bash
python3 alkemy.py
```

## License 🧾
The MIT License (MIT)

![](https://i.pinimg.com/originals/a4/9d/89/a49d89969bd34bb144e6fb9664d825a1.gif)
