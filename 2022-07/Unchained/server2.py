#!/usr/bin/env python3

from flask import Flask, Response, request

app = Flask(__name__)

# Ah, heck, you got me. It's been Flask the whole time!

@app.route('/')
def index():
    return Response(open(__file__).read(), mimetype='text/plain')

@app.route('/flag')
def flag():
    if 'user' not in request.args:
        return "User not logged in!"
    if request.args['user'] != 'admin':
        return "User is not admin!"
    return f"Welcome, {request.args['user']}! The flag is {open('flag.txt').read()}"
    
app.run('0.0.0.0', 1337)

