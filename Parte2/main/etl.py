import pandas as pd
import psycopg2
import os
import logging
import time
from sqlalchemy import create_engine
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

def wait_for_db():
    db_host = os.getenv("POSTGRES_HOST", "db")
    db_name = os.getenv("POSTGRES_DB", "etl_db")
    db_user = os.getenv("POSTGRES_USER", "user")
    db_password = os.getenv("POSTGRES_PASSWORD", "password")
    
    logging.info("Esperando a que PostgreSQL esté disponible...")
    
    for _ in range(10):  # Reintenta por 50 segundos (10 intentos x 5 seg cada uno)
        try:
            conn = psycopg2.connect(
                host=db_host,
                database=db_name,
                user=db_user,
                password=db_password
            )
            conn.close()
            logging.info("Base de datos lista. Continuando con ETL...")
            return
        except psycopg2.OperationalError:
            logging.warning("Base de datos no disponible. Reintentando en 5 segundos...")
            time.sleep(5)
    
    logging.error("No se pudo conectar a la base de datos después de varios intentos.")

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
    wait_for_db()
    load_csv_to_postgres()
