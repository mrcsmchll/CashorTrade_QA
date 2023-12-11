# database.py
import sqlite3

class Database:
    def __init__(self, db_file="test_database.db"):
        self.conn = sqlite3.connect(db_file)
        self.create_tables()

    def create_tables(self):
        # Create tables if they don't exist
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    mail TEXT NOT NULL,
                    phone TEXT NOT NULL
                )
            ''')

            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS sale_posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    title TEXT NOT NULL,
                    description TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')

    def insert_user(self, username, mail, phone):
        with self.conn:
            cursor = self.conn.execute("INSERT INTO users (username, mail, phone) VALUES (?, ?, ?)", (username, mail, phone))
            return cursor.lastrowid

    def insert_sale_post(self, user_id, title, description):
        with self.conn:
            cursor = self.conn.execute("INSERT INTO sale_posts (user_id, title, description) VALUES (?, ?, ?)", (user_id, title, description))
            return cursor.lastrowid
