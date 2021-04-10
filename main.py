from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'loggin'

@app.route('/first')
def module1():
    return 'Hello, World'

if __name__ == "__main__":
    app.run(host='0.0.0.0')