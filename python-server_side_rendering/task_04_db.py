#!/usr/bin/python3
"""flask app showing products from json csv or sqlite"""

import csv
import json
import os
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def _base_dir():
    """base dir for data files"""
    return os.path.dirname(__file__)


def load_products_from_json():
    """read products from products.json"""
    path = os.path.join(_base_dir(), "products.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError):
        return []
    raw = data if isinstance(data, list) else data.get("products", [])
    items = []
    for item in raw:
        if not isinstance(item, dict):
            continue
        try:
            pid = int(item.get("id"))
            price = float(item.get("price"))
        except (TypeError, ValueError):
            continue
        items.append(
            {
                "id": pid,
                "name": str(item.get("name", "")),
                "category": str(item.get("category", "")),
                "price": price,
            }
        )
    return items


def load_products_from_csv():
    """read products from products.csv"""
    path = os.path.join(_base_dir(), "products.csv")
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except OSError:
        return []
    items = []
    for row in rows:
        try:
            pid = int(row.get("id"))
            price = float(row.get("price"))
        except (TypeError, ValueError):
            continue
        items.append(
            {
                "id": pid,
                "name": row.get("name", ""),
                "category": row.get("category", ""),
                "price": price,
            }
        )
    return items


def load_products_from_sql():
    """read products from sqlite db"""
    db_path = os.path.join(_base_dir(), "products.db")
    items = []
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for pid, name, category, price in rows:
            items.append(
                {
                    "id": int(pid),
                    "name": str(name),
                    "category": str(category),
                    "price": float(price),
                }
            )
    except sqlite3.Error:
        return None
    finally:
        try:
            conn.close()
        except Exception:
            pass
    return items


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
    """items page still works in this app"""
    path = os.path.join(_base_dir(), "items.json")
    data = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = json.load(f).get("items", [])
            if isinstance(raw, list):
                data = [str(v) for v in raw]
    except (OSError, json.JSONDecodeError):
        data = []
    return render_template("items.html", items=data)


@app.route("/products")
def products():
    """show products from json csv or sql with optional id filter"""
    source = request.args.get("source", type=str)
    id_value = request.args.get("id", default=None, type=str)

    error = None
    products = []
    id_requested = id_value is not None
    product_id = None

    # handle id parsing
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
        elif source == "sql":
            products = load_products_from_sql()
            if products is None:
                error = "Database error"
        else:
            error = "Wrong source"

    # filter by id when needed
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
