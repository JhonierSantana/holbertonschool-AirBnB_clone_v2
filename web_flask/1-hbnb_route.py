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


if __name__ == '__main__':
    app.run(host='0.0.0.0')
