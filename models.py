from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt

db = SQLAlchemy()
# bcrypt = Bcrypt()

# DO NOT MODIFY THIS FUNCTION


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
