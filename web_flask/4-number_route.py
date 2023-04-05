#!/usr/bin/python3
''' Star flask'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def index_2():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def index_3(text):
    return "C {}".format(text).replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def index_4(text='is cool'):
    return "Python {}".format(text).replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def index_4(n):
    return "{} is number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
