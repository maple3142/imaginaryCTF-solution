#!/usr/bin/env python3.9

from flask import Flask, render_template_string, request

app = Flask(__name__)


@app.route('/')
def index():
    return ("\x3cpre\x3e\x3ccode\x3e%s\x3c/code\x3e\x3c/pre\x3e")%open(__file__).read()


@app.route('/ssti')
def check():
    flag = open("flag.txt", 'r').read().strip()
    if "input" in request.args:
        query = request.args["input"]
        render_template_string(query)
        return "Thank you for your input."
    return "No input found."

@app.route('/ssti2')
def check2():
    flag = open("flag.txt", 'r').read().strip()
    if "input" in request.args:
        query = request.args["input"]
        return render_template_string(query)
    return "No input found."

app.run('0.0.0.0', 5555)
