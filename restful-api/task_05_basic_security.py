#!/usr/bin/env python3



from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)

# app setup -> this is just setup/config and doesn’t enforce auth by itself
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "dev-secret-key-change-me"

# auth helpers -> actual authentication mechanisms -> to protect routes and issue/verify tokens.
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# in memory users with hashed passwords and roles
users = {
    "user1":  {"username": "user1",  "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"},
}

# basic auth verification
@auth.verify_password
def verify_pw(username, password):
    u = users.get(username)
    if not u:
        return None
    if check_password_hash(u["password"], password):
        return username
    return None

# basic auth protected route
@app.get("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# jwt login route
@app.post("/login")
def login():
    # validate, is it json? and credentials
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 401
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 401

    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Missing credentials"}), 401

    u = users.get(username)
    if not u or not check_password_hash(u["password"], password):
        return jsonify({"error": "Bad credentials"}), 401

    # create token with role claim
    claims = {"role": u["role"]}
    token = create_access_token(identity=username, additional_claims=claims)
    return jsonify({"access_token": token}), 200


# jwt protected route
@app.get("/jwt-protected")
@jwt_required()
def jwt_protected():
    who = get_jwt_identity()
    return f"JWT Auth: Access Granted ({who})"

# admin only route with role check
@app.get("/admin-only")
@jwt_required()
def admin_only():
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# jwt error handlers return 401 for auth errors
@jwt.unauthorized_loader
def handle_missing_token(err_msg):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token(err_msg):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

# local run
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

