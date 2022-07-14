import os
import subprocess
from app import create_app
import threading, webbrowser
from werkzeug.serving import run_simple
from flask import *


app = create_app()


if __name__ == "__main__": 

    url = "http://127.0.0.1:8080"

    threading.Timer(1.25, lambda: webbrowser.open(url) ).start()
    run_simple('127.0.0.1', 8080, app)
