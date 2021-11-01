#!/usr/bin/env python3.9

from flask import Flask, render_template_string, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["10000 per hour"]
)


@limiter.limit("5/second", override_defaults=True)
@app.route('/')
def index():
    return ("\x3cpre\x3e\x3ccode\x3e%s\x3c/code\x3e\x3c/pre\x3e")%open(__file__).read()


@limiter.limit("5/second", override_defaults=True)
@app.route('/ssti')
def check():
    flag = open("flag.txt", 'r').read().strip()
    if "input" in request.args:
        query = request.args["input"]
        render_template_string(query)
        return "Thank you for your input."
    return "No input found."


app.run('0.0.0.0', 5555)
