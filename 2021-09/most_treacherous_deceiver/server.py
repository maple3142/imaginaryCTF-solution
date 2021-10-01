from flask import Flask, jsonify, request, render_template
from flask_caching import Cache
from base64 import b64decode
from pathlib import Path

from timeout_decorator import timeout
from multiprocessing import Process
from time import sleep, time

from Crypto.Util.number import getPrime
from secrets import choice, randbelow

from strange import check_submission, get_keywords
from algo import algos


IP = "127.0.0.1"
server = Flask(__name__)
controller = Flask(__name__)

cache = Cache()
cache.init_app(app=server, config={"CACHE_TYPE": "FileSystemCache", "CACHE_DIR": Path("/tmp")})
last_token = "last_token"
port = "port"        # attack surface
token = "token"      # detection surface
op_code = "op_code"  # prevention surface

# super secure TRNG
m = getPrime(128)
a = randbelow(m)
c = randbelow(m)

# super secure RSA
p = getPrime(1024)
q = getPrime(1024)


@server.route("/flag", methods=["GET"])
def get_flag():
    user_token = request.args.get("token")
    current_token = None
    with server.app_context():
        current_token = str(cache.get(token))

    if user_token == current_token:
        return render_template("flag.html")
    else:
        return "<p>Please enter a valid token via /flag?token=*your_token*</p>"


@controller.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@controller.route("/token", methods=["POST"])
def check_token():
    if not request.is_json: 
        return jsonify({
            "message": "only application/json allowed",
            "hint": "requests.post(*url*, json={*your_data*})",
            "status_code": 400
        })

    predicted_token = request.json.get("predictedToken")
    if not predicted_token or type(predicted_token) is not int:
        return jsonify({
            "message": "predictedToken must be a positive non-zero int",
            "statusCode": 400
        })

    future_token = request.json.get("futureToken")
    if not future_token or type(future_token) is not int:
        return jsonify({
            "message": "futureToken must be a positive non-zero int",
            "statusCode": 400
        })

    hint = current_token = 0
    with server.app_context():
        hint = cache.get(last_token)
        current_token = cache.get(token)

    if predicted_token != current_token:
        return jsonify({
            "message": "predictedToken did not match the current token",
            "lastToken": hint, # this is just BM, you can't even use it anymore
            "statusCode": 403
        })

    else:
        t = current_token
        for _ in range(int(str(current_token)[1]) + 2):
            t = next_token(t)

        if future_token != t:
            return jsonify({
                "message": "futureToken did not match actual future token",
                "statusCode": 403
            })
        else:
            current_op_code = {}
            with server.app_context():
                current_op_code = cache.get(op_code)
            return jsonify({
                    "message": "Wow, you must be a real hacker. \
                    Plese solve these algos for me, I'll even give you my flag.",
                    "algos": "\n".join([str(a) for a in algos]),
                    "opCode": current_op_code
                })

@controller.route("/algo", methods=["POST"])
def check_user_algos():
    if not request.is_json: 
        return jsonify({
            "message": "only application/json allowed",
            "hint": "requests.post(*url*, json={*your_data*})",
            "status_code": 400
        })

    user_algos = request.json.get("algos")
    if not user_algos or type(user_algos) is not list or len(user_algos) != 5:
        return jsonify({
            "message": "algos must be of type list and must contain 5 algos",
            "statusCode": 400
        })

    try:
        translation = None
        with server.app_context():
            translation = cache.get(op_code)

        for i in range(len(algos)):
            is_same, user_out = check_submission(user_algos[i], algos[i], translation)
            if not is_same:
                return jsonify({
                        "message": f"Sadly algorithm nr. {i} did not work. I really need them to work, so no flag for you.",
                        "statusCode": 400,
                        "algoOutput": "<REDACTED>",
                        "userOutput": user_out
                    })

        current_port = None
        with server.app_context():        
            current_port = cache.get(port)

        return jsonify({
            "message": f":rooPOG: You did it! Here's your flag:",
            "port": current_port
        })
    except BaseException as e:
        return jsonify({
                "message": "Please don't exploit me :rooNobooli:",
                "statusCode": 500,
                "error": str(e)
            })


def start_server():
    print("\n[#] Starting server...")
    server.run(IP, cache.get(port))


def start_controller():
    print("\n[#] Starting controller...")
    controller.run(IP, 9003)


# this is even faster than secrets.randbelow() and still very secure
def next_token(current_token):
    return (a * current_token + c) % m


# RSA and xor?! pliz help
def next_port():
    nonce = int(time()*1000)
    key = randbelow(2**128)
    return (pow(nonce, 0x10001, p*q) ^ nonce) % 2**15 + 2**15 


def next_op_code():
    return get_keywords()


def mtd_init():
    with server.app_context():
        cache.set(token, 1)


def mtd_action():
    with server.app_context():
        current_token = cache.get(token)
        cache.set(last_token, current_token)
        cache.set(token, next_token(current_token))
        cache.set(port, next_port())
        cache.set(op_code, next_op_code())


def defender2000():
    controller_process = None
    while True:
        try:
            controller_process = Process(target=start_controller)
            controller_process.start()
            mtd_init()
            sleep(1) # wait for init to complete

            while True:
                mtd_action()

                server_process = Process(target=start_server)
                server_process.start()
                sleep(3)
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
            sleep(1)


if __name__ == "__main__":
    defender2000()
