#!/usr/bin/env python3
"""Task 4: Simple API using Flask.

Endpoints:
- GET  /                → "Welcome to the Flask API!"
- GET  /data            → JSON list of usernames
- GET  /status          → "OK"
- GET  /users/<username>→ JSON user object or 404 {"error":"User not found"}
- POST /add_user        → create user from JSON with validations
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage: username -> user dict
# NOTE: leave empty for checker
users = {}


@app.get("/")
def home():
    # plain text welcome
    return "Welcome to the Flask API!"


@app.get("/data")
def list_usernames():
    # return only the list of usernames (JSON array)
    return jsonify(sorted(users.keys()))


@app.get("/status")
def status():
    return "OK"


@app.get("/users/<username>")
def get_user(username: str):
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.post("/add_user")
def add_user():
    # Validate JSON body
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Save user (store whole object; key = username)
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    # For local testing (checker uses flask CLI)
    app.run(host="127.0.0.1", port=5000)
