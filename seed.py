from models import db, User, Plan


db.drop_all()
db.create_all()

# c1 = Cupcake(
#     flavor="cherry",
#     size="large",
#     rating=5,
# )

# c2 = Cupcake(
#     flavor="chocolate",
#     size="small",
#     rating=9,
#     image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
# )

user = User(
    username="adreosch21",
    password="password123",
    first_name="Austin",
    last_name="Dreosch",
    email="austindreosch@gmail.com",
    subscribed=True
)

plan1 = Plan(
    price=29.99,
    serving_count=2,
    meal_count=3,
    image_url="https://previews.dropbox.com/p/thumb/ABuMVgPe56wgbequNbDR8xaFGbgtz6Qh6PNKPPOriJSib7FVm9ltPGn0Nli8gT8G6XsKA9V6VB8WehKprMAP_UCpPc8Tn3ghnIQEOsk-DyOgTIUyhifhwAY9ONv-wo3J6R7ZcICC4T12E_K7V99piqE7rll9cJ27utQgDsrQrhO2NyTwlT0_n_PE06kcvZ5aHLLN7lGhTwqz-nYDzwm5mhp1qcOXiHu9lAOnZVb1P7eV1upBQhp0IDsuHytYJ5jia5pUTQcu-XFMtXAvfsrErRFZdoA54C8EULfIMFEtWf60fqKTf9W_kyIY7zxATzpgpCFvl3u_mSU6Ix-9YUi3EHjZQYKQjAQFK1E7_R0RLltkTA2Ztd78XPV94KcO-DYPvlQ/p.png",

)

db.session.add_all()
db.session.commit()
