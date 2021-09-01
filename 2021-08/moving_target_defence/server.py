#!/usr/local/bin/python3

from flask import Flask, jsonify, request, render_template
from flask_caching import Cache
from pathlib import Path

from multiprocessing import Process
from threading import Thread
from time import sleep

from random import choice, randint, randrange
from string import ascii_letters


IP = "0.0.0.0"
server = Flask(__name__)
controller = Flask(__name__)

cache = Cache()
cache.init_app(app=server, config={"CACHE_TYPE": "filesystem",'CACHE_DIR': Path('/tmp')})
port, token = "PORT", "TOKEN"
cache.set(port, 1234)
cache.set(token, "A" * 64)


@server.route("/flag", methods=["GET"])
def get_flag():    
    with server.app_context():
        if request.args.get('token') == cache.get(token):
            return render_template("flag.html")

        else:
            return "<p>Please enter a valid token via /flag?token=*your_token*</p>"


@controller.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@controller.route("/state", methods=["GET"])
def get_state():
    with server.app_context():
        return jsonify({
            "port": cache.get(port),
            "token": cache.get(token)
            })


def start_server():
    print("\n[#] Starting server...")
    server.run(IP, cache.get(port))


def start_controller():
    print("\n[#] Starting controller...")
    controller.run(IP, 9001)


def change_port():
    with server.app_context():
        cache.set(port, randint(1024, 8096))


def change_token():
    with server.app_context():
        cache.set(token, "".join([choice(ascii_letters) for _ in range(64)]))


def defender2000():
    while True:        
        try:
            controller_process = Process(target=start_controller)
            controller_process.start()

            while True:
                change_port()
                change_token()

                server_process = Process(target=start_server)
                server_process.start()
                sleep(randrange(30, 60) / 10)
                server_process.terminate()
                server_process.join()

        except KeyboardInterrupt:    
            controller_process.terminate()
            controller_process.join()
            break

        except Exception as e:
            controller_process.terminate()
            controller_process.join()
            print("\n[!] O no, someone crashed the server!\n") # just restart it
            print(e)
            sleep(2)


if __name__ == "__main__":
    defender2000()
        