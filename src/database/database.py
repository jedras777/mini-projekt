import sqlite3
from datetime import datetime


class DatabaseManager:
    def __init__(self, path):
        self.connection = sqlite3.connect(path)

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS History (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            algorithm TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
        """
        self.connection.execute(query)
        self.connection.commit()

    def insert_data(self, text: str, algorithm: str)-> None:
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "INSERT INTO History (data, algorithm, created_at) VALUES (?, ?, ?);"
        self.connection.execute(query,(text, algorithm, created_at))
        self.connection.commit()
        #todo DODAJ KOLUMNE TYP OPERACJI SZYFROWANIE/ CZY DESZYFROWANIE

    def read_data(self)-> list:
        query = "SELECT * FROM History;"
        data = self.connection.execute(query).fetchall()
        return data

    def __enter__(self):
        self.create_table()
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()

        self.connection.close()

