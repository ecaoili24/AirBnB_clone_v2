#!/usr/bin/python3
"""
A script that starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """ Returns a string at the root route"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Returns the desired string for /hbnb route"""
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    """
    Returns a string for for /c/<text> route, replace _ with space
    """
    return "C {}".format(text.replace("_", " "))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
