from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

username = "maya.papaya"
password = "1234"
facebook_friends=["Noa","Mayar","Shalev 1", "Shalev 2", "Avigail", "Ella"]


@app.route('/', methods=['GET','POST'])  # '/' for the default page
def login():
  if request.method =='POST':
  	username1  = request.form['username']
  	password1 = request.form['password']
  	if username1 == username and password1 == password:
  		return redirect(url_for('home'))
  else:
  	return render_template('login.html')
 
@app.route('/home', methods=['GET','POST']) 
def home():
	return render_template('home.html',facebook_friends=facebook_friends)

@app.route('/friend_exists/<string:name>', methods=['GET','POST'])
def friend_exists(name):
	return render_template('friend_exists.html', n=name , facebook_friends=facebook_friends)
	


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)