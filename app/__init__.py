"""Flask app."""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from .auth import auth
from .config import Config
from .models import UserModel

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    return UserModel.query(user_id)


def create_app():
    """Creates flask app."""
    app = Flask(__name__)
    boostrap = Bootstrap(app)

    app.config.from_object(Config)

    login_manager.init_app(app)

    app.register_blueprint(auth)

    return app
