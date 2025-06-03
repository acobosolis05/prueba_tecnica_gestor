from typing import Tuple, Dict, List
from pathlib import Path
import pandas as pd

cwd = Path.cwd()  

DATA_FOLDER: str = "data" 
MODELS_FOLDER: str = "models"
UTILS_FOLDER: str = "utils"


DEMAND_DATA_FILE: str = "dataset_demand_acumulate.csv"  
ALFA_BETHA_FILE: str = "dataset_alpha_betha.csv"  
TO_PREDICT: str = "to_predict.csv"  

PATH_DEMAND_DATA_FILE = cwd / DATA_FOLDER / DEMAND_DATA_FILE
PATH_ALFA_BETHA_FILE = cwd / DATA_FOLDER / ALFA_BETHA_FILE
PATH_TO_PREDICT = cwd / DATA_FOLDER / TO_PREDICT

SCALER_MODEL = "scaler_model.joblib"
CLASSIFIER_MODEL = "classifier_model.joblib"

PATH_SCALER_MODEL: str = cwd / MODELS_FOLDER / SCALER_MODEL
PATH_CLASSIFIER_MODEL: str = cwd / MODELS_FOLDER / CLASSIFIER_MODEL

LABEL_ENCODER_FILE: str = "label_encodings.json"

PATH_LABEL_ENCODER_FILE: str = cwd / UTILS_FOLDER / LABEL_ENCODER_FILE
