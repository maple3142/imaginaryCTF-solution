from flask import Flask, request, session, current_app, jsonify, Response
from lxml import etree
from lxml.etree import XMLSyntaxError

app = Flask(__name__, static_url_path='/')
app.secret_key = 'TEST_KEY'

with open('users.xml') as f:
    users = etree.parse(f)

@app.route("/", methods=["GET"])
def home():
    return current_app.send_static_file('index.html')

@app.route("/api/login", methods=["POST"])
def login():
    request_parser = etree.XMLParser(resolve_entities=False, no_network=True)
    try:
        request_xml = etree.fromstring(request.data, request_parser)
    except XMLSyntaxError:
        return jsonify(error="Invalid xml"), 400

    username = request_xml.findtext("USER")
    password = request_xml.findtext("PASSWORD")

    if not username or not password:
        return jsonify(error="Missing username or password"), 400
        
    result = users.xpath(f"/USERS/USER[NAME/text()='{username}' and PASSWORD/text()='{password}']/NAME/text()")
    
    if result:
        session['user'] = result[0]
        return jsonify(username=result[0])
    else:
        return jsonify(error="Wrong username or password"), 401

@app.route("/api/logout", methods=["POST"])
def logout():
    session.clear()
    return Response(status=200)

@app.route("/api/admin", methods=["POST"])
def admin():
    if not 'user' in session or session['user'] != 'admin':
        return jsonify(error="Only admin can access this endpoint"), 401
    
    request_parser = etree.XMLParser(resolve_entities=True)
    try:
        request_xml = etree.fromstring(request.data, request_parser)
    except XMLSyntaxError:
        return jsonify(error="Invalid xml"), 400

    username = request_xml.findtext("USER")
    if not username:
        return jsonify(error="Missing username"), 400
    if username == 'admin':
        return jsonify(error="Can't get admin password"), 400

    password = request_xml.findtext("PASSWORD")
    if password != users.xpath("/USERS/USER[NAME/text()=$username]/PASSWORD/text()", username='admin')[0]:
        return jsonify(error="Incorrect admin password"), 401

    result = users.xpath("/USERS/USER[NAME/text()=$username]/PASSWORD/text()", username=username)

    if result:
        return jsonify(username=username, password=result[0])
    else:
        return jsonify(username=username)

@app.route("/api/checksession", methods=["POST"])
def checksession():
    if 'user' in session:
        return jsonify(username=session['user'])
    return Response(status=404)