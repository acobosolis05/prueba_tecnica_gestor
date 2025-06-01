from typing import Tuple, Dict, List
from pathlib import Path
import pandas as pd

cwd = Path.cwd()  # Obtiene el directorio de trabajo actual como objeto Path

DATA_FOLDER: str = "data"  # Nombre de la carpeta donde están los datos

DEMAND_DATA_FILE: str = "dataset_demand_acumulate.csv"  # Nombre del archivo de datos de DEMANDA
ALFA_BETHA_FILE: str = "dataset_alpha_betha.csv"  # Archivo de clasificacion 
TO_PREDICT: str = "to_predict.csv"  # 


# Construye las rutas completas a los archivos de datos usando el directorio actual y la carpeta de datos
PATH_DEMAND_DATA_FILE = cwd / DATA_FOLDER / DEMAND_DATA_FILE
PATH_ALFA_BETHA_FILE = cwd / DATA_FOLDER / ALFA_BETHA_FILE
PATH_TO_PREDICT = cwd / DATA_FOLDER / TO_PREDICT
