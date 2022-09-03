#!/usr/bin/python3
"""Write a script that starts a Flask web application"""


from flask import Flask

app = Flask(__name__)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    @app.route("/", strict_slashes=False)
    def hello_hbnb():
        """when request route "/" displays “Hello HBNB!”"""
        return(f"Hello HBNB!")
