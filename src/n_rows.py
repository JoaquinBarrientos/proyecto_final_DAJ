from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from generals import CONN

def row_number():
    query = """
    SELECT COUNT(1) FROM tlc_ny.yellow.yellow_taxi_trips
    """
    try:
        with CONN.connect() as connection:
            result = connection.execute(text(query))
            return result.fetchall()
    except SQLAlchemyError as e:
        print(f"Error al conectar o ejecutar la consulta: {e}")
        return None

if __name__ == "__main__":
    print(row_number())
