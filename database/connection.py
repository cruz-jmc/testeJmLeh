import os
import sqlite3

def get_connection():
    db_path = os.path.join("database", "grupoLehJm")
    return sqlite3.connect()