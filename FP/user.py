from database import DB

class User:
	def __init__(self, id, username, mail, address, mobile, password):
		self.id = id
		self.username = username
		self.mail = mail
		self.address = address
		self.mobile = mobile
		self.password = password

	def create(self):
		with DB() as db:  
			values = (self.username, self.mail, self.address, self.mobile, self.password)
			db.execute('''
				INSERT INTO Users (username, mail, address, mobile, password)
				VALUES (?, ?, ?, ?, ?)''', values)
			return self

	@staticmethod
	def load(mail, password):
		with DB() as db:
			values = db.execute("SELECT * from Users WHERE mail = ?  AND password = ? ", (mail,password,)).fetchone()
			
		return User(*values)
			
			
			
	def verify_password(self, password):
		return self.password == password
