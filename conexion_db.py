import logging
import glob
# from decouple import config
# from sqlalchemy import create_engine as ce
import pandas as pd

logging.basicConfig(
    format = '%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s', 
    level=logging.DEBUG, 
    filename='alkemy.log',  
    encoding="utf-8"
    )


files = glob.glob('.//**//**//' + '*.csv')
# print(files)
for f in files:
    print(f)
    data = pd.read_csv(f,
                       header = 0,
                       sep = ',')
    # print(data.to_markdown())
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(data)

# try:
#     pg_engine = ce(config('engine_psql'))
#     logging.info("Conexión exitosa.")
#     connection = pg_engine.raw_connection()
#     cursor = connection.cursor()
#     cursor.execute("SELECT version()")
#     row = cursor.fetchone()
#     logging.info("Versión del servidor de PostgreSQL: {}".format(row))
#     # cursor.execute("SELECT * FROM ago22")
#     # rows = cursor.fetchall()
#     # for row in rows:
#     #     print(row)

# except Exception as ex:
#     logging.error("Error durante la conexión: {}".format(ex))

# finally:
#     pg_engine.dispose()
#     logging.info("La conexión ha finalizado.")
    