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
    Returns a string for /c/<text> route, replace _ with space
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/<text>')
def python_is_magic(text):
    """
    Returns a string for /python/<text> route, replace _ with space
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/python/')
def python_is_cool():
    """
    Returns a default string for /python/ route
    """
    text = 'is cool'
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def is_a_number(n):
    """
    Return a string only if it's a valid integer
    """
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
