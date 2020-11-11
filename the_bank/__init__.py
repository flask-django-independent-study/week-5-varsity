"""Import libraries."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Here we import Praetorian from flask_praetorian
from flask_praetorian import Praetorian
from the_bank.config import Config

db = SQLAlchemy()
# TODO: Initialize Praetorian as guard


def create_app(model, config_class=Config):
    """Create an instance of the bank app."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    # TODO: call init_app on guard and pass in app and model
    # model is the database class which we want to use to authenticate
    # throughout our app. The reason we are not initializing init_app with
    # Account is because we are importing "db" in our models. Importing
    # "Account" in this file would cause a circular import. The simplest
    # way around this is to get the database class as an argument and pass the
    # arguement into init_app. We will pass the argument into the app next when
    # we initalize the app in the app.py file.

    from the_bank.main.routes import main
    from the_bank.api.routes import api

    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix="/api")

    with app.app_context():
        db.create_all()

    return app


# TODO: go to app.py
