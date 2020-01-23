#from database import DB
import sqlite3 as sql

#con = sql.connect('database.db')
#con.execute('CREATE TABLE IF NOT EXISTS User (ID IINTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,' + 'Username TEXT NOT NULL UNIQUE, Password TEXT NOT NULL)')
#con.close

class User:
    def __init__(self, id, username, password, mail, address, mobile):
        self.id = id
        self.username = username
        self.password = password
        self.mail = mail
        self.address = address
        self.mobile = mobile
        

    def create(self):
        with DB() as db:
            values = (self.username, self.password)
            db.execute('''
                INSERT INTO Users (username, mail, address, mobile, password)
                VALUES (?, ?, ?, ?, ?)''', values)
            return self
     
    def verify_password(self, password):
        return self.password == password
		
