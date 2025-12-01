#!/usr/bin/python3
"""basic flask app using jinja templates"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """home page"""
    return render_template("index.html")


@app.route("/about")
def about():
    """about page"""
    return render_template("about.html")


@app.route("/contact")
def contact():
    """contact page"""
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
