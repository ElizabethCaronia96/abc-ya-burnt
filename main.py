from flask import Flask
app = Flask(__name__)

def app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])

@app.route('/')
def index():
    return 'loggin'

@app.route('/first')
def module1():
    return 'Hello, World'
