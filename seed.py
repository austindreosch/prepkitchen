from models import db, User, Plan, Order
# from app import db

db.drop_all()
db.create_all()

# users
user = User(
    username="adreosch21",
    password="password123",
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
# order1 = Order(
#     user_id=1,
#     plan_id=2,
#     meal_id1=52819,
#     meal_id2=52960,
#     meal_id3=52995,
#     meal_id4=52864,
#     meal_id5=53010
# )


db.session.add(user)
db.session.add(plan1)
db.session.add(plan2)
db.session.add(plan3)
# db.session.add(order1)
db.session.commit()
