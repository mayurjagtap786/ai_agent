from pathlib import Path
from sqlite3 import Connection


class ApplicationService:
    CORPUS_DIR = Path(__file__).parent.parent.parent / 'corpus'

    def __init__(self, db_connection:Connection):
        self.db_connection = db_connection




