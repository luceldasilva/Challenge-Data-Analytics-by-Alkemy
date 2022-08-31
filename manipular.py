import logging
import glob
import pandas as pd


logging.basicConfig(
    format = '%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s', 
    level=logging.DEBUG, 
    filename='alkemy.log',  
    encoding="utf-8"
    )


def manipulation():
    files = glob.glob('.//**//**//' + '*.csv')
    for f in files:
        logging.info(f)
        data = pd.read_csv(f,
                        header = 0,
                        sep = ',')
        if 'Departamento' in data.columns:
            data.drop(['Departamento'], axis=1)
        if 'Subcategoria' in data.columns:
            data.drop(['Subcategoria'], axis=1)
        if 'subcategoria' in data.columns:
            data.drop(['subcategoria'], axis=1)
        data = data.rename(columns={data.columns[0]: 'cod_localidad', 
                                    data.columns[1]: 'id_provincia',
                                    data.columns[2]: 'id_departamento',
                                    data.columns[3]: 'ojo',
                                    data.columns[4]: 'categoría',
                                    data.columns[5]: 'provincia',
                                    data.columns[6]: 'localidad',
                                    data.columns[7]: 'nombre',
                                    data.columns[8]: 'domicilio',
                                    data.columns[9]: 'piso',
                                    data.columns[10]: 'código_postal',
                                    data.columns[11]: 'codigo_tel',
                                    data.columns[12]: 'teléfono',
                                    data.columns[13]: 'mail',
                                    data.columns[14]: 'web'})
        data.to_csv(f, index=False, encoding='utf-8')
        logging.info('archivo actualizado')


def run():
    logging.info('Empieza manipulación de archivos')
    manipulation()

if __name__ == '__main__':
    run()




