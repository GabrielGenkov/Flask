from flask import Flask, redirect, url_for, request, render_template

from user import User
from post import Post

#from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)

class Store:
	def __init__(self):
		self.user = None
	
	def run(self):
		
		@app.route('/register', methods=['GET', 'POST'])
		def register():
			if request.method == 'GET':
				return render_template('register.html')
			elif request.method == 'POST':
				values = (
					None,
					request.form['username'], 
					request.form['mail'],
					request.form['address'],
					request.form['mobile'],
					request.form['password']
					)
				self.user = User(*values).create()
				return redirect('/')

		@app.route('/', methods=['GET', 'POST'])
		def login():
			if request.method == "GET":
				return render_template('index.html',user = self.user, posts = Post.all())
			if request.method == "POST":
				mail = request.form['mail']
				password = request.form['password']
				self.user = User.load(mail, password)
			return render_template('index.html',user = self.user, posts = Post.all())

		@app.route('/logout')
		def logout():
			self.user = None
			return redirect('/')

		@app.route('/posts/new', methods=['GET', 'POST'])
		def new_post():
			if not self.user:
				return redirect('/')
			if request.method == 'GET':
				return render_template('new_post.html')
			elif request.method == 'POST':
				values = (
					None,
					self.user,
					request.form['title'],
					request.form['info'],
					request.form['price'],
				)
				Post(*values).create()
			return redirect('/')
		
		@app.route('/posts/my_posts')
		def my_posts():
			if not self.user:
				return redirect('/')
			return render_template('my_posts.html',user = self.user, posts = Post.all())
	
		@app.route('/posts/my_cart')
		def my_cart():
			if not self.user:
				return redirect('/')
			return render_template('my_cart.html',user = self.user, posts = Post.all())
		
		@app.route('/posts/<int:id>/delete')
		def delete(id):
			if not self.user:
				return redirect('/')
			post = Post.find(id)
			if post.user == self.user.id:
				post.delete()
			return redirect('/')
	
		@app.route('/posts/<int:id>/buy')
		def buy(id):
			if not self.user:
				return redirect('/')
			post = Post.find(id)
			if post.user == self.user.id:
				return redirect('/')
			Post.bought(post.id, self.user.id)
			return redirect('/')
		
		@app.route('/posts/<int:id>/edit', methods=['GET', 'POST'])
		def edit(id):
			if not self.user:
				return redirect('/')
			post = Post.find(id)
			if post.user != self.user.id:
				return redirect('/')
			if request.method == 'GET':
				return render_template('edit_post.html', post = post)
			elif request.method == 'POST':
				values = (
					id,
					None,
					request.form['title'],
					request.form['info'],
					request.form['price'],
					None,
					None,
					None
				)
				Post(*values).save()
			return redirect('/')


if __name__ == '__main__':
	store = Store()
	store.run()
	app.run(debug = True)
