#!/usr/bin/env python3

from flask import Flask, Response, request, redirect
from time import time

from secret import SECRET_PASSWORD
from jwt import JWT

app = Flask(__name__)

@app.route('/')
def index():
    return Response(open(__file__).read(), mimetype='text/plain')

@app.route('/jwt')
def jwt():
    return Response(open('jwt.py').read(), mimetype='text/plain')

@app.route('/login')
def login():
    if 'password' in request.args and request.args['password'] == SECRET_PASSWORD:
        username = 'admin'
    else:
        username = 'boring_user'
    token = JWT({'username': username, "created": int(time())})
    resp = redirect('/flag', 302)
    resp.set_cookie("token", str(token))
    return resp

@app.route('/flag')
def check():
    token_str = request.cookies.get('token')
    if token_str is None:
        return "Not logged in!"
    token = JWT.from_str(token_str)
    if not token.validate():
        return "Error validating token!"
    print(token.data['username'])
    if token.data['username'] != "admin":
        return "Not an admin!"
    return f"Admin logged in! {open('flag.txt').read()}"


app.run('0.0.0.0', 2002)
