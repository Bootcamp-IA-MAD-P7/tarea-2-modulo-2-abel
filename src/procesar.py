# src/procesar.py

import logging
import sys
from pathlib import Path
import pandas as pd

# 1. Definir rutas del proyecto de forma dinámica
RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
CARPA_RAW = RAIZ_PROYECTO / "data" / "raw"
CARPA_PROCESSED = RAIZ_PROYECTO / "data" / "processed"

# 2. Configurar la carpeta y el archivo de logs
CARPETA_LOGS = RAIZ_PROYECTO / "logs"
CARPETA_LOGS.mkdir(exist_ok=True)  # Crea la carpeta logs/ si no existe
RUTA_LOG_FILE = CARPETA_LOGS / "proyecto.log"

# 3. Configuración avanzada del Logger
logger = logging.getLogger("proyecto_data")
logger.setLevel(logging.INFO)

# Evitar que los logs suban al manejador raíz por defecto de Jupyter
logger.propagate = False

# Limpiar manejadores previos si el notebook recarga el archivo.py
if logger.hasHandlers():
    logger.handlers.clear()

# Formato común para los mensajes de registro
formato = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Manejador A: Guarda los logs en el archivo físico logs/proyecto.log
file_handler = logging.FileHandler(RUTA_LOG_FILE, encoding='utf-8')
file_handler.setFormatter(formato)
logger.addHandler(file_handler)

# Manejador B: Envía los logs exclusivamente a la Terminal Estándar (sys.stdout)
stream_handler = logging.StreamHandler(sys.__stdout__)
stream_handler.setFormatter(formato)
logger.addHandler(stream_handler)

def cargar_datos_seguro(nombre_archivo: str) -> pd.DataFrame:
    """Carga un archivo desde la carpeta data/raw registrando eventos en terminal y archivo log."""
    ruta_completa = CARPA_RAW / nombre_archivo
    
    if not ruta_completa.exists():
        logger.error(f'Error de lectura: No existe el archivo en la ruta {ruta_completa}')
        raise FileNotFoundError(f'No se encontró el archivo en: {ruta_completa}')
        
    logger.info(f'Iniciando la lectura del archivo CSV: {nombre_archivo}')
    
    df = pd.read_csv(ruta_completa)
    
    logger.info(f'Archivo {nombre_archivo} cargado exitosamente. Dimensiones: {df.shape}')
    return df