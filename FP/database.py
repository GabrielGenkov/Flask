import sqlite3

DB_name = 'database.db'

conn = sqlite3.connect(DB_name)

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS Users
    (
        id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		username	TEXT NOT NULL UNIQUE,
		mail	TEXT NOT NULL UNIQUE,
		address	TEXT NOT NULL,
		mobile	INTEGER NOT NULL UNIQUE,
		password	TEXT NOT NULL
    )
''')

class DB:
    def __enter__(self):
        self.conn = sqlite3.connect(DB_name)
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
