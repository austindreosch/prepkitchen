from flask import Flask, render_template, request, redirect, session
import requests
from models import connect_db, db
# from sqlalchemy.exc import IntegrityError
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///prepkitchen'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
app.config['SECRET_KEY'] = ("very_secret")

connect_db(app)
# db.create_all()

# https://postimg.cc/gallery/yZCM7f4  postimg link


CURR_USER_KEY = "current_user"


@app.route("/")
def index():
    """Home page."""

    return render_template("index.html")


@app.route('/plans')
def show_plans():
    """Show plans page. Leads to ordering page."""

    return render_template('plans.html')

# simple api call for menu getting


@app.route('/menu/<category_str>')
def query(category_str):

    heading = "Menu"

    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category_str}"
    response = requests.get(url)

    data = response.json()
    meals = data['meals']
    selected_meals = []

    for meal in range(len(meals)):
        selected_meals.append(meals[meal])

    return render_template('menu.html', selected_meals=selected_meals, heading=heading, category_str=category_str)


@app.route('/choose')
def menu_choose():

    heading = "Choose your meals."
    cart = []

    if 'cart_array' in session:
        cart = session['cart_array']
        # this works, but its returned a string instead of a list

    cart_list = cart.split(", ")

    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=Seafood"
    response = requests.get(url)

    data = response.json()
    meals = data['meals']
    selected_meals = []

    for meal in range(len(meals)):
        selected_meals.append(meals[meal])

    return render_template('menu-choose.html', selected_meals=selected_meals, heading=heading, cart_list=cart_list)


@app.route("/cart", methods=["POST"])
def shopping_cart():
    """API for shopping_cart saving."""
    cart_array = []

    # should be able to do this without loop
    keys = request.form.keys()
    for key in keys:
        cart_array = key

    print(cart_array)

    # add cart_array to user session
    session['cart_array'] = cart_array

    return redirect('/choose')


@app.route("/cart/clear", methods=["POST"])
def cart_clear():
    """POST for clearing cart session."""

    if 'cart_array' in session:
        session['cart_array'] = []

    return redirect('/choose')


# @ app.route('/choose/post', methods=['POST'])
# def menu_choose_post():

#     heading = "Choose your meals."

#     url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=Seafood"
#     response = requests.get(url)

#     data = response.json()
#     meals = data['meals']
#     selected_meals = []

#     for meal in range(len(meals)):
#         selected_meals.append(meals[meal])

#     return redirect('/choose')


# USERS
# ####################
@ app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data, form.password.data)

        if user:
            session[CURR_USER_KEY] = user.id

        flash("Welcome! You have logged in successfully.")
        return redirect("/")

    return render_template('login.html', form=form)


@ app.route('/register', methods=["GET", "POST"])
def signup():
    """Handle user signup.
    Create new user and add to DB. Redirect to home page.
    If form not valid, present form.
    If the there already is a user with that username: flash message
    and re-present form.
    """

    form = RegisterForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data,
                password=form.password.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                subscribed=form.subscribed.data
            )

            order = Order()
            db.session.commit()

        except IntegrityError:
            flash("Username already taken", 'danger')
            return render_template('register.html', form=form)

        do_login(user)

        return redirect("/")

    else:
        return render_template('register.html', form=form)
