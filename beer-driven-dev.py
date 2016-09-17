# -*- coding: utf-8 -*-
__author__ = 'aosn'

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()