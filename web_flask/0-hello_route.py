#!/usr/bin/python3
<<<<<<< HEAD
""" 0. Script to start a Flask web application """

from flask import Flask


=======
"""Starts Flask web app
Listening on 0.0.0.0:5000
Route '/' displays "Hello HBNB!"
"""
from flask import Flask

>>>>>>> 5b18bfbd20053619b84f584f55bbdfeba6abbdb3
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def hello_world():
    """ Returns some text. """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======
def hello_route():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
>>>>>>> 5b18bfbd20053619b84f584f55bbdfeba6abbdb3
