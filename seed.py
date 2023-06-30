from models import db, User, Plan, Order
from app import db
from flask_bcrypt import Bcrypt
from datetime import datetime

bcrypt = Bcrypt()

db.drop_all()
db.create_all()

# users
user1 = User(
    username="adreosch21",
    password=bcrypt.generate_password_hash("password123").decode("utf-8"),
    first_name="Austin",
    last_name="Dreosch",
    email="austindreosch@gmail.com",
    address_street="234 Westgate St.",
    address_city="San Vicardo",
    address_state="CA",
    address_zip="84561"
)

# plans
plan1 = Plan(
    price=29.99,
    serving_count=2,
    meal_count=3,
    image_url="https://i.postimg.cc/5fBHLzDx/plan1.png",
    active=True
)
plan2 = Plan(
    price=49.99,
    serving_count=2,
    meal_count=5,
    image_url="https://i.postimg.cc/VsymZ8ZJ/plan2.png",
    active=True
)
plan3 = Plan(
    price=64.99,
    serving_count=4,
    meal_count=4,
    image_url="https://i.postimg.cc/wznqjXx9/plan3.png",
    active=True
)

# orders
# Look up the user based on the username
# user = User.query.filter_by(username="adreosch21").first()
db.session.add(user1)
db.session.commit()

# Only create an order if the user exists
order = Order(
    user_id=user1.id,
    plan_id=1,  # Assuming the plan with ID 1 exists
    date=datetime.utcnow(),
    billing_name="John Doe",
    billing_card="1234567890123456",
    billing_code="123",
    billing_street="123 Main St",
    billing_city="San Francisco",
    billing_state="CA",
    billing_zip="12345",
    price=29.99,
    tax=0.0,
    total=29.99,
    meal_id1=53036,
    meal_id2=52895,
    meal_id3=53041
)

# Add the order to the session and commit the changes


db.session.add(plan1)
db.session.add(plan2)
db.session.add(plan3)
db.session.add(order)
db.session.commit()
