from flask import Flask, jsonify,Blueprint
from .auth import auth_bp


def create_app():
    app = Flask(__name__)
    return app

