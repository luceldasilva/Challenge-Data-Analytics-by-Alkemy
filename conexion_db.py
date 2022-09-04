import logging
from os.path import abspath
from pathlib import Path
import pyprojroot
from decouple import config
from sqlalchemy import create_engine as ce
import numpy as np
import pandas as pd

logging.basicConfig(
    format = '%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s', 
    level=logging.DEBUG, 
    filename='alkemy.log',  
    encoding="utf-8"
    )

def manipulation_sql():
    try:
        pg_engine = ce(config('engine_psql'))
        logging.info("Conexión exitosa.")
        connection = pg_engine.raw_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT version()")
        row = cursor.fetchone()
        logging.info("Versión del servidor de PostgreSQL: {}".format(row))
        with open(str(abspath('table_create.sql')), 'r', encoding='utf-8') as myfile:
            tc = myfile.read()
            cursor.execute(tc)
            logging.info("Tabla creada")
        sql = '''INSERT INTO alkemy (cod_localidad, id_provincia, id_departamento, categoría, provincia, localidad, nombre, domicilio, código_postal, codigo_tel, teléfono, mail, web, fuente)
                VALUES 
                    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        files = Path(str(pyprojroot.here('data'))).glob("**/*.csv")
        for f in files:
            logging.info(f)
            data = pd.read_csv(f,header = 0, sep = ',')
            if 'Departamento' in data.columns:
                data = data.drop(['Departamento'], axis=1)
            if 'Subcategoria' in data.columns:
                data = data.drop(['Subcategoria'], axis=1)
            if 'subcategoria' in data.columns:
                data = data.drop(['subcategoria'], axis=1)
            data = data.rename(columns={data.columns[0]: 'cod_localidad', data.columns[1]: 'id_provincia', data.columns[2]: 'id_departamento', data.columns[3]: 'ojo', data.columns[4]: 'categoría',
                                        data.columns[5]: 'provincia', data.columns[6]: 'localidad', data.columns[7]: 'nombre', data.columns[8]: 'domicilio', data.columns[9]: 'estas_filas',
                                        data.columns[10]: 'código_postal', data.columns[11]: 'codigo_tel', data.columns[12]: 'teléfono', data.columns[13]: 'mail', data.columns[14]: 'web',
                                        data.columns[15]: 'las_voy', data.columns[16]: 'a_borrar', data.columns[17]: 'porque_no', data.columns[18]: 'las_usaré', data.columns[19]: 'fuente',}
                                        )
            # Limpiando datos
            logging.info('Limpiando datos y ordenando')
            data = data.replace(['s/d'], np.nan)
            data = data.replace(['Gobierno de la provincia'], ['Gobierno de la Provincia'])
            data = data.replace(['Gob. Pcia.'], ['Gobierno de la Provincia'])
            data = data.replace(['RCC- Córdoba'], ['RCC'])
            data = data.replace(['Santa Fé'], ['Santa Fe'])
            data = data.replace(['Tierra del Fuego, Antártida e Islas del Atlántico Sur'], ['Tierra del Fuego'])
            data = data.replace(['Ciudad Autónoma de Buenos Aires'], ['Capital Federal'])
            data = data.replace(['Espacios de Exhibición Patrimonial'], ['Museos'])
            data = data.drop(['ojo', 'estas_filas', 'las_voy', 'a_borrar', 'porque_no', 'las_usaré'], axis=1)
            data.provincia = data.provincia.str.strip() # Había espacios en blanco surtidos
            data = data.iloc[:, :14]
            logging.info('Hacer insert into * from alkemy')
            list_data = data.values.tolist()
            cursor.executemany(sql, list_data)
            connection.commit()
            logging.info('archivo agregado a la tabla')
        logging.info('Preparando tabla alkemy para consultas')
        df = pd.read_sql_table("alkemy", pg_engine)
        cat_count_df = df.groupby(['categoría'])['categoría'].count() 
        fuente_count_df = df.groupby(['fuente'])['fuente'].count().sort_values(ascending=0)
        province_df = df.groupby(['provincia','categoría']).size().reset_index(name='total').sort_values('provincia', ascending=1)
        with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.precision', 3,):
            fly = 0    
            butter = [str(cat_count_df), str(fuente_count_df), str(province_df)]
            print(".·-=-·." * 11)
            while fly < 3:
                print(butter[fly]) #juego de palabras
                print(".·-=-·." * 11)
                fly += 1 

    except Exception as ex:
        logging.error("Error durante la conexión: {}".format(ex))

    finally:
        pg_engine.dispose()
        logging.info("La conexión ha finalizado.")
    
def run():
    manipulation_sql()

if __name__ == '__main__':
    run()

    