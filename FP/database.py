import sqlite3

DB_name = 'database.db'

conn = sqlite3.connect(DB_name)

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS Users
    (
        id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		username	TEXT NOT NULL,
		mail	TEXT NOT NULL UNIQUE,
		address	TEXT NOT NULL,
		mobile	INTEGER NOT NULL UNIQUE,
		password	TEXT NOT NULL
    )
''')

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS Posts 
	(
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	user	INTEGER,
	title	TEXT NOT NULL,
	info	TEXT NOT NULL,
	price	INTEGER NOT NULL,
	date	TEXT NOT NULL,
	isActive	INTEGER,
	buyer	INTEGER,
	FOREIGN KEY(user) REFERENCES Users ( id ),
	FOREIGN KEY(buyer) REFERENCES Users ( id )
	)
''')
conn.commit()

class DB:
    def __enter__(self):
        self.conn = sqlite3.connect(DB_name)
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
