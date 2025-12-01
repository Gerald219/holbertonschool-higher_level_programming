#!/usr/bin/python3
"""flask app that shows products from json or csv"""

import csv
import json
import os
from flask import Flask, render_template, request

app = Flask(__name__)


def _base_dir():
    """base folder for this module"""
    return os.path.dirname(__file__)


def load_products_from_json():
    """load products from products.json"""
    path = os.path.join(_base_dir(), "products.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError):
        return []
    # sometimes list, sometimes under key
    if isinstance(data, list):
        raw_products = data
    else:
        raw_products = data.get("products", [])
    products = []
    for item in raw_products:
        if not isinstance(item, dict):
            continue
        try:
            pid = int(item.get("id"))
            price = float(item.get("price"))
        except (TypeError, ValueError):
            continue
        products.append(
            {
                "id": pid,
                "name": str(item.get("name", "")),
                "category": str(item.get("category", "")),
                "price": price,
            }
        )
    return products


def load_products_from_csv():
    """load products from products.csv"""
    path = os.path.join(_base_dir(), "products.csv")
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except OSError:
        return []
    products = []
    for row in rows:
        try:
            pid = int(row.get("id"))
            price = float(row.get("price"))
        except (TypeError, ValueError):
            continue
        products.append(
            {
                "id": pid,
                "name": row.get("name", ""),
                "category": row.get("category", ""),
                "price": price,
            }
        )
    return products


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
    """keep items page working for this app"""
    path = os.path.join(_base_dir(), "items.json")
    items_list = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            raw = data.get("items", [])
            if isinstance(raw, list):
                items_list = [str(v) for v in raw]
    except (OSError, json.JSONDecodeError):
        items_list = []
    return render_template("items.html", items=items_list)


@app.route("/products")
def products():
    """show products from json or csv, optional id filter"""
    source = request.args.get("source", type=str)
    id_value = request.args.get("id", default=None, type=str)

    error = None
    products = []
    id_requested = id_value is not None
    product_id = None

    # try to parse id if given
    if id_requested:
        try:
            product_id = int(id_value)
        except ValueError:
            error = "Product not found"

    if not error:
        if source == "json":
            products = load_products_from_json()
        elif source == "csv":
            products = load_products_from_csv()
        else:
            error = "Wrong source"

    # filter by id when we have one and no source error
    if not error and id_requested and product_id is not None:
        filtered = [p for p in products if p.get("id") == product_id]
        if not filtered:
            error = "Product not found"
            products = []
        else:
            products = filtered

    return render_template("product_display.html", products=products, error=error)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
