#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import werkzeug.exceptions as ex
from calculator import MyCalculator
from super_token import MyToken

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hello.html")

@app.route("/token")
def token():
    token = MyToken().generate_token()
    return render_template("token.html", token=token)

@app.route("/calculatrice", methods=['POST', 'GET'])
def calculatrice():
    if request.method == 'POST':
        dict_operation = request.form
        result = MyCalculator().calculate(dict_operation)
    else:
        result = ''
    return render_template("calculatrice.html", result=result)

if __name__ == "__main__":
    app.run()
