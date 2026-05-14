import os
import psycopg2

from dotenv import load_dotenv
load_dotenv()

DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_DATABASE = os.getenv("POSTGRES_DB")
DB_HOST = os.getenv("POSTGRES_HOST")

conn = psycopg2.connect("dbname=postgres",
                            user=DB_USER,
                            password=DB_PASSWORD,
                            dbname=DB_DATABASE,
                            host=DB_HOST,
                            port="5432")
cursor = conn.cursor()
print("Conectado com sucesso")