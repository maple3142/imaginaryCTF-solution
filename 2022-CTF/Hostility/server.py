#!/usr/bin/env python3

from requests import get
from flask import Flask, Response, request
from time import sleep
from threading import Thread
from os import _exit

app = Flask(__name__)

class Restart(Thread):
    def run(self):
        sleep(30)
        _exit(0) # killing the server after 5 minutes, and docker should restart it

Restart().start()

@app.route('/')
def index():
    return Response(open(__file__).read(), mimetype='text/plain')

@app.route('/docker')
def docker():
    return Response(open("Dockerfile").read(), mimetype='text/plain')

@app.route('/upload', methods=["GET"])
def upload_get():
    return open("upload.html").read()

@app.route('/upload', methods=["POST"])
def upload_post():
    if "file" not in request.files:
        return "No file submitted!"
    file = request.files['file']
    if file.filename == '':
        return "No file submitted!"
    file.save("./uploads/"+file.filename)
    return f"Saved {file.filename}"

@app.route('/flag')
def check():
    flag = open("flag.txt").read()
    get(f"http://localhost:1337/{flag}")
    return "Flag sent to localhost!"

app.run('0.0.0.0', 1337)