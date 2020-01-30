from database import DB
from datetime import date


class Post:
	def __init__(self, id, user, title, info, price, date = date.today(), isActive = True, buyer = 0):
		self.id = id
		self.user = user
		self.title = title
		self.info = info
		self.price = price
		self.date = date
		self.isActive = isActive
		self.buyer = buyer

	@staticmethod
	def all():
		with DB() as db:
			rows = db.execute('SELECT * FROM Posts').fetchall()
			return [Post(*row) for row in rows]

	@staticmethod
	def find(id):
		with DB() as db:
			row = db.execute(
				'SELECT * FROM Posts WHERE id = ?',
				(id,)
			).fetchone()
		return Post(*row)

	@staticmethod
	def find_by_user(user_id):
		with DB() as db:
			rows = db.execute(
				'SELECT * FROM Posts WHERE user = ?',
				(userId,)
			).fetchall()
		return [Post(*row) for row in rows]

	def create(self):
		with DB() as db:
			values = (self.user.id, self.title, self.info, self.price, self.date, self.isActive, self.buyer)
			db.execute('''
				INSERT INTO Posts (user, title, info, price, date, isActive, buyer)
				VALUES (?, ?, ?, ?, ?, ?, ?)''', values)
			return self

	def save(self):
		with DB() as db:
			values = (
				self.title,
				self.info,
				self.price,
				self.id
			)
			db.execute(
				'''UPDATE Posts
				SET title = ?, info = ?, price = ?
				WHERE id = ?''', values)
			return self

	@staticmethod
	def bought(post_id, user_id):
		with DB() as db:
			db.execute("UPDATE Posts SET isActive = 0, buyer = ? WHERE id = ?", (user_id, post_id))
	
	def delete(self):
		with DB() as db:
			db.execute('DELETE FROM Posts WHERE id = ?', (self.id,))
