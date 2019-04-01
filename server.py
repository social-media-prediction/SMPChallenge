#-*-coding:utf-8-*-

from flask import Flask, render_template, request, jsonify, make_response
from hashlib import md5
import sqlite3

app = Flask(__name__)
app.debug = True

SUCCESS = '00000'
PARAMETER_ERROR = '10001'
USERNAME_EXIST = '10002'
PASSWORD_TOO_SHORT = '10003'
EMAIL_EXIST = '10004'
TOKEN_NOT_EXIST = '10005'
EMAIL_NOT_EXIST = '10006'
PASSWORD_ERROR = '10007'

conn = sqlite3.connect('smp.db')
cursor = conn.cursor()

def send_verify_email(username, password, email):
	return SUCCESS

def check_login(email, password):
	return SUCCESS

def token2uid(token):
	return 'uid', True

def uid2username(uid):
	return "Bo Wu"

@app.route('/', methods=['GET'])
def index():
	cookies = request.cookies
	print cookies.keys()
	if not 'token' in cookies:
		return render_template('index.html')
	token = cookies['token']
	print token
	uid, status = token2uid(token)
	if status == False:
		res = make_response(render_template('index.html'))
		res.delete_cookie('token')
		return res

	username = uid2username(uid)
	res = make_response(render_template('index.html', login=True, username=username))
	res.set_cookie('token', token)
	return res

@app.route('/challenge', methods=['GET'])
def challenge():
	cookies = request.cookies
	print cookies.keys()
	if not 'token' in cookies:
		return render_template('challenge.html')
	token = cookies['token']
	print token
	uid, status = token2uid(token)
	if status == False:
		res = make_response(render_template('challenge.html'))
		res.delete_cookie('token')
		return res

	username = uid2username(uid)
	res = make_response(render_template('challenge.html', login=True, username=username))
	res.set_cookie('token', token)
	return res

@app.route('/dataset', methods=['GET'])
def dataset():
	cookies = request.cookies
	print cookies.keys()
	if not 'token' in cookies:
		return render_template('dataset.html')
	token = cookies['token']
	print token
	uid, status = token2uid(token)
	if status == False:
		res = make_response(render_template('dataset.html'))
		res.delete_cookie('token')
		return res

	username = uid2username(uid)
	res = make_response(render_template('dataset.html', login=True, username=username))
	res.set_cookie('token', token)
	return res

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
	cookies = request.cookies
	print cookies.keys()
	if not 'token' in cookies:
		return render_template('leaderboard.html')
	token = cookies['token']
	print token
	uid, status = token2uid(token)
	if status == False:
		res = make_response(render_template('leaderboard.html'))
		res.delete_cookie('token')
		return res

	username = uid2username(uid)
	res = make_response(render_template('leaderboard.html', login=True, username=username))
	res.set_cookie('token', token)
	return res

@app.route('/register', methods=['POST'])
def register():
	form = request.form
	required = ['username', 'password', 'email']
	for key in required:
		if not key in form:
			return jsonify(code=PARAMETER_ERROR)

	username = form['username']
	password = form['password']
	email = form['email']

	res = send_verify_email(username, password, email)

	return jsonify(code=res)

@app.route('/verify/<code>', methods=['GET'])
def verify(code):
	username, password, email = check_verify(code)

	if username != None:
		adduser(username, password, email)

	return jsonify(code=SUCCESS)

@app.route('/login', methods=['POST'])
def login():
	form = request.form
	required = ['email', 'password']
	for key in required:
		if not key in form:
			return jsonify(code=PARAMETER_ERROR)

	email = form['email']
	password = form['password']

	res = check_login(email, password)
	#add cookie
	res = jsonify(code=res)
	res.set_cookie('token', '1234')
	return res

@app.route('/get_status', methods=['GET'])
def get_status():
	cookies = request.cookies
	if not 'token' in cookies:
		return jsonify(code=TOKEN_NOT_EXIST)
	token = cookies['token']
	uid, status = token2uid(token)
	if status == False:
		return jsonify(code=TOKEN_NOT_EXIST)

	info = uid2info(uid)
	return jsonify(code=SUCCESS, info=info)

@app.route('/update_team', methods=['POST'])
def update_team():
	cookies = request.cookies
	if not 'token' in cookies:
		return jsonify(code=TOKEN_NOT_EXIST)
	token = cookies['token']
	uid, status = token2uid(token)
	if status == False:
		return jsonify(code=TOKEN_NOT_EXIST)

	form = request.form
	if not 'team' in form:
		return jsonify(code=PARAMETER_ERROR)

	team = form['team']

	res = update_info_by_uid(uid, team)
	return jsonify(code=res)

@app.route('/forget_password', methods=['POST'])
def forget_password():
	form = request.form
	if not 'email' in form:
		return jsonify(code=PARAMETER_ERROR)

	email = form['email']
	res = check_email_exist(email)
	if res == False:
		return jsonify(code=EMAIL_NOT_EXIST)

	send_reset_email(email)
	return jsonify(code=SUCCESS)

@app.route('/reset_password/<code>', methods=['GET'])
def reset_password(code):
	form = request.form
	if not 'password' in form:
		return jsonify(code=PARAMETER_ERROR)

	password = form['password']
	uid = code2uid(code)
	res = check_update(uid, password)
	return jsonify(code=res)

@app.route('/logout', methods=['POST'])
def logout():
	res = make_response(jsonify(code=SUCCESS))
	res.delete_cookie("token")
	return res

if __name__ == '__main__':
	app.run('0.0.0.0', 5000)