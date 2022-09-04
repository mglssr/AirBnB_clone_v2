#!/usr/bin/python3
"""Write a script that starts a Flask web application"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """when request route "/" displays “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """generic comment"""
    return "HBNB"


@app.route("/c/<txt>", strict_slashes=False)
def c_(txt):
    """generic comment"""
    txt = txt.replace("_", " ")
    return "C {}".format(txt)


@app.route("/python", strict_slashes=False)
@app.route("/python/(<txt>)", strict_slashes=False)
def python_(txt):
    """generic comment"""
    if not txt:
        txt = "is cool"
    else:
        txt = txt.replace("_", " ")
    return "Python {}".format(txt)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
