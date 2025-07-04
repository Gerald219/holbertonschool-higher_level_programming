#!/usr/bin/python3
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API!"
# In-memory users dictionary (empty at start)
users = {}

@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

if __name__ == "__main__":
    app.run()
