from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

# DO NOT MODIFY THIS FUNCTION


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """Users model."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    address_street = db.Column(db.Text, nullable=False)
    address_city = db.Column(db.Text, nullable=False)
    address_state = db.Column(db.Text, nullable=False)
    address_zip = db.Column(db.Text, nullable=False)
    orders = db.relationship('Order', backref='users')

    @classmethod
    def register(cls, username, pwd, first_name, last_name, email, address_street, address_city, address_state, address_zip):

        hashed = bcrypt.generate_password_hash(pwd)

        hash_str = hashed.decode("utf8")

        return cls(username=username, password=hash_str, first_name=first_name, last_name=last_name, email=email, address_street=address_street, address_city=address_city, address_state=address_state, address_zip=address_zip)

    @classmethod
    def authenticate(cls, username, pwd):

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, pwd):
            return user
        else:
            return False


class Plan(db.Model):
    """Plans model."""
    __tablename__ = 'plans'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.Float, nullable=False)
    serving_count = db.Column(db.Integer, nullable=False)
    meal_count = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.Text, nullable=False)
    active = db.Column(db.Boolean, default=True)


class Order(db.Model):
    """Orders model."""
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    plan_id = db.Column(db.Integer, db.ForeignKey('plans.id'))
    date = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow()
    )
    billing_name = db.Column(db.Text, nullable=False)
    billing_card = db.Column(db.Text, nullable=False)
    billing_code = db.Column(db.Text, nullable=False)
    billing_street = db.Column(db.Text, nullable=False)
    billing_city = db.Column(db.Text, nullable=False)
    billing_state = db.Column(db.Text, nullable=False)
    billing_zip = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    tax = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    meal_id1 = db.Column(db.Integer, nullable=False)
    meal_id2 = db.Column(db.Integer, nullable=False)
    meal_id3 = db.Column(db.Integer, nullable=False)
    meal_id4 = db.Column(db.Integer)
    meal_id5 = db.Column(db.Integer)

