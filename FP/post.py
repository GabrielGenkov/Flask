from database import DB
from datetime import date


class Post:
    def __init__(self, id, user, title, info, price, date = date.today(), isActive = True, buyer = None):
        self.id = id
        self.user = user
        self.title = title
        self.info = info
        self.price = price

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
                'SELECT * FROM Posts WHERE user_id = ?',
                (userId,)
            ).fetchall()
            return [Post(*row) for row in rows]

    def create(self):
        with DB() as db:
            values = (self.user.id, self.title, self.info, self.price, date.today(), True, 0)
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
				self.isActive,
				self.buyer
            )
            db.execute(
                '''UPDATE Posts
                SET title = ?, info = ?, price = ?, isActive = ?, Buyer = ?
                WHERE id = ?''', values)
            return self

    def delete(self):
        with DB() as db:
            db.execute('DELETE FROM Posts WHERE id = ?', (self.id,))
