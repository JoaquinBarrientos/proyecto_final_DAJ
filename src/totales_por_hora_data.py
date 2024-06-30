"""
Con este codigo se crea un archivo .parquet llamado totalels_por_hora en los cuales se resume la informacion de 
la base de datos en cuanto a los totales y promedios de viajes, pasajeros y ganancias obtenidas desde el 
01/01/2023
"""
import os
import pandas as pd
from generals import CONN

# Ruta completa del directorio donde quieres guardar el archivo
output_dir = r"C:/Users/joaqu/OneDrive/Documentos/KODIGO/Projects/python_Cods/proyecto_final_DAJ/files_dump/summary_data"

# Crear directorio si no existe (en tu caso ya existe, pero esto es una buena práctica)
os.makedirs(output_dir, exist_ok=True)

# Realizar la consulta SQL
query ="""
SELECT vendorid, 
        date_trunc('hour', tpep_pickup_datetime) AS pickup_hour,
        avg(passenger_count) as avg_passenger_count,
        sum(passenger_count) as total_passenger_count,
        avg(trip_distance) as avg_trip_distance,
        sum(trip_distance) as total_trip_distance,
        avg (fare_amount) as avg_fare_amount,
        sum (fare_amount) as total_fare_amount,
        count (*) as total_trips
FROM yellow.yellow_taxi_trips
WHERE tpep_pickup_date >='2023-01-01'
GROUP BY vendorid,
        pickup_hour
"""

# Ejecutar la consulta y guardar los resultados
df_resumido = pd.read_sql(query, CONN)
df_resumido.to_parquet(os.path.join(output_dir, "totales_por_hora.parquet"))