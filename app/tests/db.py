import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import OperationalError
import time

from app.tests.config import settings

def get_db_connection():
    while True:
        try:
            connection = psycopg2.connect(
                host=settings.database_host,
                user=settings.database_user,
                password=settings.database_password,
                database=settings.database_name,
                cursor_factory=RealDictCursor
            )
            cursor = connection.cursor()
            print("Database connection successful")
            break
        except Exception as error:
            print(f"Database connection failed: {error}")
            time.sleep(2)   

    return connection, cursor        