"""Import os and dotenv."""
import os
from dotenv import load_dotenv

# TODO: create a .env file with the SECRET_KEY and SQLALCHEMY_DATABASE_URI
# HINT: if you get a "drivername" error try exporting to the terminal
# as well as having them in your .env file. i.e.
# export SECRET_KEY=secret


class Config:
    """Config class."""

    ENV = "development"
    DEBUG = True
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = True


# TODO: before we really get into it feel free to run the app and see how it
# looks. Be sure to notice any changes or places where the app breaks. Don't
# worry, we'll fix all of this together.

# TODO: go to the_bank/models.py
