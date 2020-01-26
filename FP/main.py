from flask import Flask, redirect, url_for, request, render_template
from user import User
import sqlite3
DB_name = 'database.db'

conn = sqlite3.connect(DB_name)


app = Flask(__name__)




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
		User(*values).create()
		
		return redirect('/')

@app.route('/index', methods=['GET', 'POST'])
def login():
	if request.method == "GET":
		return render_template('index.html',user = user)
	if request.method == "POST":
		mail = request.form['mail']
		password = request.form['password']
		user = User.load(mail, password)
	return render_template('index.html',user = user)

@app.route('/')
def Hello():
	return render_template('index.html', user = None)
	


if __name__ == '__main__':
   app.run(debug = True)
