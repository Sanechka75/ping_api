import psycopg2

DB_CONFIG = {
        "dbname": "pingdb",
        "user": "admin",
        "password": "secret",
        "host": "localhost",
        "port": 5433
        }

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute ("""
    CREATE TABLE IF NOT EXISTS pings (
    id SERIAL PRIMARY KEY,
    ip VARCHAR(15) NOT NULL,
    status VARCHAR(10) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    cur.close()
    conn.close()

def save_ping(ip, status):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO pings (ip, status) VALUES (%s, %s)", (ip, status))
    conn.commit()
    cur.close()
    conn.close()

def get_pings(ip):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT ip, status, created_at FROM pings WHERE ip = (%s)", (ip,))
    # conn.commit() не нужен, т.к. данные не меняем, чисто читаем
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
