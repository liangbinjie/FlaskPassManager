import os
import subprocess
from app import create_app
import threading, webbrowser
from werkzeug.serving import run_simple
from flask import *
from waitress import serve


app = create_app()


if __name__ == "__main__": 

    url = "http://127.0.0.1:8000"

    threading.Timer(1.25, lambda: webbrowser.open(url) ).start()
    app.run(port=8000)
