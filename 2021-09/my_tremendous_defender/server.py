from flask import Flask, jsonify, request, render_template
from flask_caching import Cache
from pathlib import Path

from multiprocessing import Process
from time import sleep

from random import choice, randint, randrange
from string import ascii_letters
from os import urandom
from re import search

IP = "0.0.0.0"
server = Flask(__name__)
controller = Flask(__name__)

cache = Cache()
cache.init_app(app=server, config={"CACHE_TYPE": "filesystem", "CACHE_DIR": Path("/tmp")})
port, token, password_requirements, signing_key = "PORT", "TOKEN", "PASSWORD_REQUIREMENTS", "SIGNING_KEY"


@server.route("/flag", methods=["GET"])
def get_flag():
    with server.app_context():
        if request.args.get("token") == cache.get(token):
            return render_template("flag.html")

        else:
            return "<p>Please enter a valid token via /flag?token=*your_token*</p>"


@controller.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@controller.route("/accessToken", methods=["POST"])
def get_access_token():
    if not request.is_json: 
        return jsonify({
            "message": "only application/json allowed",
            "hint": "requests.post(*url*, json={*your_data*})",
            "status_code": 400
        })

    password = request.json.get("password")
    if not password or type(password) is not str:
        return jsonify({
            "message": "password must be a string",
            "statusCode": 400
        })

    with server.app_context():
        pw_req = cache.get(password_requirements)

    if not search(pw_req, password):
        return jsonify({
            "message": "your password does not comply with the current password requirements",
            "pwReq": pw_req,
            "statusCode": 401
        })

    with server.app_context():
        key = cache.get(signing_key)

    pw_int = int.from_bytes(password.encode(), "big")
    signed = pw_int ^ key
    return jsonify({
        "message": "access token created",
        "statusCode": 200,
        "signedPassword": signed
    })


@controller.route("/state", methods=["POST"], )
def get_state():
    if not request.is_json: 
        return jsonify({
            "message": "only application/json allowed",
            "hint": "requests.post(*url*, json={*your_data*})",
            "status_code": 400
        })

    signed_pw = request.json.get("signedPassword")

    if signed_pw is None or type(signed_pw) is not int:
        return jsonify({
            "message": "\"signedPassword\" must an integer",
            "status_code": 400
        })


    with server.app_context():
        sk = cache.get(signing_key)

    if signed_pw ^ sk == 1337:
        with server.app_context():
            return jsonify({
                "port": cache.get(port),
                "token": cache.get(token),
                "statusCode": 200
            })
    else:
        return jsonify({
            "message": "password forgery detected",
            "statusCode": 403
        })


def start_server():
    print("\n[#] Starting server...")
    server.run(IP, cache.get(port))


def start_controller():
    print("\n[#] Starting controller...")
    controller.run(IP, 9002)


def create_new_password_req():
    # One does not simply "Generate a String that matches a RegEx in Python" -> secure
    charsets = ["[a-z]", "[A-Z]", "[!-/]", "[0-9]"]
    regex = "^"
    for _ in range(5):
        regex += f"{choice(charsets)}{{{randint(2, 10)}}}"
    return regex+"$"


def mtd_action():
    new_port = randint(1024, 8096)
    new_token = "".join([choice(ascii_letters) for _ in range(64)])
    new_signing_key = int.from_bytes(urandom(32), "big")
    new_password_requirements = create_new_password_req()

    with server.app_context():
        cache.set(port, new_port)
        cache.set(token, new_token)
        cache.set(signing_key, new_signing_key)
        cache.set(password_requirements, new_password_requirements)


def defender2000():
    controller_process = None
    while True:
        try:
            controller_process = Process(target=start_controller)
            controller_process.start()

            while True:
                mtd_action()

                server_process = Process(target=start_server)
                server_process.start()
                sleep(randrange(100, 150) / 10)
                server_process.terminate()
                server_process.join()

        except KeyboardInterrupt:
            controller_process.terminate()
            controller_process.join()
            break

        except Exception as e:
            controller_process.terminate()
            controller_process.join()
            print("\n[!] O no, someone crashed the server!\n")  # just restart it
            print(e)
            sleep(2)


if __name__ == "__main__":
    defender2000()
