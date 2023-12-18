from app import create_app
import webbrowser
import threading

app = create_app()

def open_browser():
    webbrowser.open('http://127.0.0.1:5000')

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()
    app.run(debug=True)


"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
"""