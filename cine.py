# from os.path import abspath
# from os.path import isdir
from pathlib import Path
import pyprojroot
# from decouple import config
# import numpy as np
import pandas as pd
# from decouple import config
from datetime import datetime
# import os


def cine():
    dir_cine = Path(str(pyprojroot.here('data').joinpath('cine'))).glob("**/*.csv")
    for buscar_cine in dir_cine:
        df_cine = pd.read_csv(buscar_cine, header = 0, sep = ',')
        print(df_cine)

if __name__ == '__main__':
    cine()