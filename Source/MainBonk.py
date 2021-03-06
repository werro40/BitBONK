# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 07:06:12 2021

@author: adila
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 08:54:13 2021

@author: adila
"""
import numpy as np
import matplotlib.pyplot as plt

from flask import Flask, redirect, url_for, render_template, request, send_from_directory


def plotter(day):
    return day;


app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
        return render_template("index.html")
    
@app.route("/bonkground")
def bonkground():
        return render_template("bonkground.html")

@app.route("/bonker", methods=["POST","GET"])
def bonker():
    if request.method == "POST":
        days = request.form["nm"]
        plotter(days)
        return redirect(url_for("bonker"))
    else:
        return render_template("bonker.html")


# @app.route('/static/<path:path>')
# def send_js(path):
#     return send_from_directory('js', path)

#@app.route("/<usr>", methods=["POST","GET"])
# user(usr):
#        return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run()


