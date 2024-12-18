import mysql.connector
from config.config import DATABASE_CONFIG

def get_connection():
    return mysql.connector.connect(**DATABASE_CONFIG)

def execute_query(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    cursor.close()
    conn.close()

def fetch_query(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
