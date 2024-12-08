from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Bye code!"

@app.route("/hello")
def greating():
    return "Hello world!"

@app.route("/sum/<int:a>/<int:b>")
def sum(a: int, b: int):
    return f"La suma es {str(a + b)}"

@app.route('/multiply/<int:a>/<int:b>")
def multiply(a: int, b: int):
    return f"La multiplicación es {str(a * b)}"
