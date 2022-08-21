from decouple import config
from sqlalchemy import create_engine as ce
import pandas as pd

try:
    pg_engine = ce(config('engine_psql'))
    print("Conexión exitosa.")
    connection = pg_engine.raw_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT version()")
    row = cursor.fetchone()
    print("Versión del servidor de PostgreSQL: {}".format(row))
    # cursor.execute("SELECT * FROM ago22")
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)

except Exception as ex:
    print("Error durante la conexión: {}".format(ex))

finally:
    pg_engine.dispose()
    print("La conexión ha finalizado.")
    