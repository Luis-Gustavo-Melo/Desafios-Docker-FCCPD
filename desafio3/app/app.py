import time
import redis
import psycopg2
import os
from flask import Flask

app = Flask(__name__)

REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
DB_HOST = os.getenv('DB_HOST', 'db')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASS = os.getenv('DB_PASS', 'senha_secreta')
DB_NAME = os.getenv('DB_NAME', 'banco_logs')

cache = redis.Redis(host=REDIS_HOST, port=6379)

def get_db_connection():
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS
            )
            return conn
        except psycopg2.OperationalError:
            retries -= 1
            print("Banco ocupado, tentando de novo em 2s...")
            time.sleep(2)
    return None

def init_db():
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS visitas (id SERIAL PRIMARY KEY, info TEXT);')
        conn.commit()
        cur.close()
        conn.close()

@app.route('/')
def hello():

    count = cache.incr('hits')
    
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO visitas (info) VALUES (%s)', (f'Visita numero {count}',))
        conn.commit()
        cur.close()
        conn.close()
        db_status = "Gravado no Postgres com sucesso!"
    else:
        db_status = "Erro ao conectar no Postgres."

    return f'<h1>Ola Docker Compose!</h1><p>Esta pagina foi vista <strong>{count}</strong> vezes.</p><p>Status do DB: {db_status}</p>'

if __name__ == "__main__":
    time.sleep(5) 
    init_db()
    app.run(host="0.0.0.0", port=5000)