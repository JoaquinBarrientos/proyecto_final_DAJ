"""
Con este codigo se crea un archivo .parquet llamado muestra db en el cual se resumen los 29k registros de la base
de datos, correspondientes a los datos de viajes realizados por taxis amarillos que sean de fecha mayor a
01/01/2023, el archivo no está en repositorio debido al tamaño de archivos permitos por GITHUB, sin embargo se puede 
generar y descargar para luego cargarlo en Power BI y realizar el analisis

"""
import os
import pandas as pd
from generals import CONN

# Ruta completa del directorio donde quieres guardar el archivo
output_dir = r"C:/Users/joaqu/OneDrive/Documentos/KODIGO/Projects/python_Cods/proyecto_final_DAJ/files_dump/summary_data"

# Crear directorio si no existe (en tu caso ya existe, pero esto es una buena práctica)
os.makedirs(output_dir, exist_ok=True)

query = """
SELECT trip_id,vendorid,payment_type,total_amount
FROM yellow.yellow_taxi_trips
where tpep_pickup_date >='2023-01-01'
"""

# Ejecutar la consulta y guardar los resultados
df_resumido = pd.read_sql(query, CONN)
df_resumido.to_parquet(os.path.join(output_dir, "muestrabd.parquet"))


