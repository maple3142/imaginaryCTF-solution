# decompyle3 version 3.7.5
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Jul  3 2021, 10:33:51) 
# [GCC 10.2.1 20210110]
# Embedded file name: loginbeta.py
# Compiled at: 2021-08-06 13:06:28
# Size of source mod 2**32: 1682 bytes
import os
from xml.dom import minidom
from base64 import b64encode
import xml.etree.ElementTree as gfg
from flask import Flask, render_template, request, render_template_string, session
app = Flask(__name__)

@app.route('/<REDACTED>', methods=['POST'])
def coolfeature():
    cookie = 'https://media.istockphoto.com/vectors/chocolate-chip-cookies-vector-id452121629?k=6&m=452121629&s=612x612&w=0&h=_sHqM8a4Q4ib98eihm6lFTDzHL4NvsmVnlYNnGR4OHk='
    username = request.form['username']
    root = gfg.Element('root')
    m1 = gfg.Element('data')
    root.append(m1)
    b1 = gfg.SubElement(m1, 'username')
    b1.text = username
    b3 = gfg.SubElement(m1, 'isAdmin')
    b3.text = 'no'
    tree = gfg.ElementTree(root)
    tree = tree.getroot()
    xml_str = gfg.tostring(tree).decode().replace('&lt;', '<').replace('&gt;', '>')
    xml_str = minidom.parseString(xml_str).toprettyxml(indent='    ')
    IMPORTANT_INFO = 'You do not need to resign the cookie and resend it; that is not what this part is about.'
    session['xml_b64'] = b64encode(xml_str.encode())
    parse_root = gfg.fromstring(xml_str)
    for child in parse_root:
        for childd in child:
            if childd.tag == 'username':
                parse_username = 'Welcome ' + childd.text
            if childd.tag == 'isAdmin':
                if childd.text == 'no':
                    is_admin = '(employee)!'
                else:
                    is_admin = '(admin)! Your flag is <REDACTED>'
                return render_template('search.html', username=parse_username, isAdmin=is_admin, cookie=cookie)
        else:
            return render_template_string('Error!')


if __name__ == '__main__':
    app.secret_key = os.getenv('KEY')
    app.config['SESSION_TYPE'] = 'redis'
    app.run(host='0.0.0.0', port=8080)
# okay decompiling newsource.pyc
