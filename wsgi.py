from app import create_app
import threading, webbrowser

app = create_app()

if __name__ == "__main__": 

    url = "http://127.0.0.1:5000"

    threading.Timer(1.25, lambda: webbrowser.open(url) ).start()
    app.run()

