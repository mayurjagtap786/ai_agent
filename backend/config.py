#Get the project root directory (parent or backend)
import os
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = bool(os.getenv('DEBUG',False))

database_path = BASE_DIR / 'backend'/ 'database.db'
database_url= f"sqlite:///{database_path}"

def dict_factory(cursor,row):
    return {col[0]: row[idx] for idx,col in enumerate(cursor.description)}

def setup_db_conn() -> sqlite3.Connection:
    connection = sqlite3.connect(database_path, isolation_level=None,check_same_thread=False)

    connection.row_factory = dict_factory

    connection.execute("PRAGMA foreign_keys = ON; ")
    connection.execute("PRAGMA journal_mode = WAL;")
    connection.execute("PRAGMA synchronous = NORMAL;")
    connection.execute("PRAGMA busy_timeout= 5000;")
    connection.execute("PRAGMA temp_store= MEMORY;")
    connection.execute("PRAGMA optimize;")

    return connection

db_connection = setup_db_conn()