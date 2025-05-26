import os

# Directorios con los PATH del proyecto

#Directorio base del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#Directorios para data cruda
RAW_DATA_DIR = os.path.join(BASE_DIR, 'data', 'raw')
RAW_DATA_PATH = os.path.join(RAW_DATA_DIR, 'raw_data.csv')

#Directorios para data procesada (posterior a data wrangling)
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, 'data', 'processed')
PROCESSED_DATA_PATH = os.path.join(PROCESSED_DATA_DIR, 'clean_data.csv')

#Directorios para data del modelo (posterior a feature engineering)
MODEL_DATA_PATH = os.path.join(PROCESSED_DATA_DIR, 'model_data.csv')