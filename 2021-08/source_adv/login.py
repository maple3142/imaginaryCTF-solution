# decompyle3 version 3.7.5
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Jul  3 2021, 10:33:51) 
# [GCC 10.2.1 20210110]
# Embedded file name: login.py
# Compiled at: 2021-07-20 12:22:10
# Size of source mod 2**32: 888 bytes
from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submission():
    username = request.form['username']
    password = request.form['pass']
    try:
        conn = sqlite3.connect('logins.db')
        c = conn.cursor()
        c.execute(f"SELECT * FROM logins WHERE username='{username}' AND password='" + password + "';")
        resp = c.fetchall()
        if resp == []:
            return render_template('index.html', error='Incorrect username or password. If this problem persists, please reach out to admin in IT.')
        return render_template('employeeportal.html', resp=(str(resp).replace("'", '')))
    except:
        return render_template('index.html', error='Something went wrong! Please try again later!')


app.run(host='0.0.0.0', port=8080)
# okay decompiling login.pyc
