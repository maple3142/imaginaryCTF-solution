#!/usr/bin/env python3

from flask import Flask, Response, request, redirect
from time import time

from jwt import JWT

app = Flask(__name__)

@app.route('/')
def index():
    return Response(open(__file__).read(), mimetype='text/plain')

@app.route('/jwt')
def jwt():
    return Response(open('jwt.py').read(), mimetype='text/plain')

@app.route('/ed25519')
def ed25519():
    return Response(open('ed25519.py').read(), mimetype='text/plain')

@app.route('/login', methods=['POST'])
def login():
    print(request.json)
    print(type(request.json))
    token = JWT(request.json)
    resp = redirect('/flag', 302)
    resp.set_cookie("token", str(token))
    return resp

@app.route('/flag')
def check():
    token_str = request.cookies.get('token')
    print(token_str)
    if token_str is None:
        return "Not logged in!"
    token = JWT.from_str(token_str)
    if not token.validate():
        return "Error validating token!"
    print(token.data['username'])
    if token.data['username'] != "admin":
        return "Not an admin!"
    return f"Admin logged in! {open('flag.txt').read()}"


app.run('0.0.0.0', 2999)
