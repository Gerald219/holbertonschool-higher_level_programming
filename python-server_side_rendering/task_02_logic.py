#!/usr/bin/python3
"""flask app showing items from a json file with jinja"""

import json
import os
from flask import Flask, render_template

app = Flask(__name__)


def load_items():
    """load items from items.json or return empty list"""
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, "items.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError):
        return []
    items = data.get("items", [])
    if not isinstance(items, list):
        return []
    return [str(item) for item in items]


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


@app.route("/items")
def items():
    """items page showing list from json"""
    items_list = load_items()
    return render_template("items.html", items=items_list)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
