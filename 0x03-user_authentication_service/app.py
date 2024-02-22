#!/usr/bin/env python3
"""flask app"""
from flask import Flask, jsonify

app = Flask(__name__)
host = "0.0.0.0"
port = "5000"


@app.route("/")
def welcome():
    """home route"""
    data = {"message": "Bienvenue"}
    return jsonify(data)


if __name__ == "__main__":
    app.run(
        host=host,
        port=port
    )
