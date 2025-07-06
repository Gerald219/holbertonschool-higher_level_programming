#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# JWT Configuration
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# Basic Auth Configuration
auth = HTTPBasicAuth()

# Basic Auth credentials
user_credentials = {
    "user1": generate_password_hash("password123"),
    "admin1": generate_password_hash("adminpassword")
}

@auth.verify_password
def verify_password(username, password):
    if username in user_credentials and check_password_hash(user_credentials.get(username), password):
        return username

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username in user_credentials and check_password_hash(user_credentials.get(username), password):
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token})
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route("/admin")
@jwt_required()
def admin_only():
    return "Admin Area"

if __name__ == "__main__":
    app.run()

