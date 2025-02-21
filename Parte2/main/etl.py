import pandas as pd
import psycopg2
import os
import logging
from sqlalchemy import create_engine
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

def load_csv_to_postgres():
    logging.info("Iniciando proceso ETL...")
    
    db_host = os.getenv("POSTGRES_HOST", "db")
    db_name = os.getenv("POSTGRES_DB", "etl_db")
    db_user = os.getenv("POSTGRES_USER", "user")
    db_password = os.getenv("POSTGRES_PASSWORD", "password")
    
    try:
        file_path = "data/data.csv"
        df = pd.read_csv(file_path)
        logging.info(f"Archivo CSV leído correctamente con {len(df)} filas.")
        
        engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}')
        
        df.to_sql('tabla_principal', engine, if_exists='replace', index=False)
        logging.info("Datos cargados exitosamente en PostgreSQL.")
    
    except Exception as e:
        logging.error(f"Error en el proceso ETL: {e}")
    
    logging.info("Proceso ETL finalizado.")
    
if __name__ == "__main__":
    load_csv_to_postgres()
