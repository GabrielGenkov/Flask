from flask import Flask, redirect, url_for, request, render_template
from user import User

app = Flask(__name__)

@app.route('/')
def Hello():
	return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html')
	elif request.method == 'POST':
		User(None,request.form['username'], request.form['mail'],request.form['address'],request.form['mobile'],request.form['password']).create()
		
		return redirect('/')

if __name__ == '__main__':
   app.run(debug = True)
