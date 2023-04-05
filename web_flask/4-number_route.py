#!/usr/bin/python3
''' Star flask'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''Second function. Prints on /hbnb'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def index_2():
    '''Second function. Prints on /hbnb'''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def index_3(text):
    '''Third function. Prints on /c/anything'''
    return "C {}".format(text).replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def index_4(text='is cool'):
     '''Fourth function. Prints on /python/anything'''
    return "Python {}".format(text).replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def index_4(n):
    '''Fifth function. Prints on number if n is int'''
    return "{} is number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
