#!/usr/bin/env python3
"""flask app"""
from flask import Flask, jsonify, request, redirect, abort
from auth import Auth


AUTH = Auth()
app = Flask(__name__)
app.url_map.strict_slashes = False
host = "0.0.0.0"
port = "5000"


@app.route("/")
def welcome():
    """home route"""
    data = {"message": "Bienvenue"}
    return jsonify(data)


@app.route("/users", methods=["POST"])
def users():
    """users route"""
    email = request.form.get("email")
    password = request.form.get("password")
    msgOk = {"email": email, "message": "user created"}
    msgErr = {"message": "email already registered"}
    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify(msgErr), 400
    return jsonify(msgOk)


@app.route("/sessions", methods=["POST"])
def login():
    """login route"""
    email = request.form.get("email")
    password = request.form.get("password")
    msgOk = {"email": email, "message": "logged in"}
    if not AUTH.valid_login(email, password):
        abort(401)
    response = jsonify(msgOk)
    response.set_cookie("session_id", AUTH.create_session(email))
    return response


@app.route("/sessions", methods=["DELETE"])
def logout():
    """logout route"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route("/profile")
def profile():
    """profile route"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route("/reset_password", methods=["POST"])
def get_reset_password_token() -> str:
    """password reset route"""
    email = request.form.get("email")
    try:
        reset_token = AUTH.get_reset_password_token(email)
        msgOk = {"email": email, "reset_token": reset_token}
    except ValueError:
        abort(403)
    return jsonify({"email": email, "reset_token": reset_token})


@app.route("/reset_password", methods=["PUT"])
def update_password() -> str:
    """password update route"""
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")
    msgOk = {"email": email, "message": "Password updated"}
    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)
    return jsonify(msgOk)


if __name__ == "__main__":
    app.run(
        host=host,
        port=port
    )
