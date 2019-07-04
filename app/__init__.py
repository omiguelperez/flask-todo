"""Flask app."""

from flask import Flask
from flask_bootstrap import Bootstrap

from .config import Config


def create_app():
    """Creates flask app."""
    app = Flask(__name__)
    boostrap = Bootstrap(app)

    app.config.from_object(Config)

    return app
