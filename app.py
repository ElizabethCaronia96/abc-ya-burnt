from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'loggin'

@app.route('/first')
def module1():
    return 'Hello, World'
