from flask import Flask, render_template, session, request, redirect, flash
import requests
from models import connect_db, db
from forms import LoginForm
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


@app.route('/plans/<int:plan_id>')
def choose_plan(plan_id):
    """Sets chosen plan in session. Then redirects to choose menu."""
    session['cart_plan_id'] = plan_id

    # if plan 1, mealCap = 3
    if plan_id == 1:
        session['meal _cap'] = 3
    elif plan_id == 2:
        session['meal _cap'] = 5
    elif plan_id == 3:
        session['meal _cap'] = 4
    else:
        # if unknown plan number
        session['meal _cap'] = 3
        session['cart_plan_id'] = 1

    return redirect('/choose/pork')


@app.route('/menu/<category_str>')
def query(category_str):
    """Normal menu, with api calls for menu change."""
    heading = "Menu"

    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category_str}"
    response = requests.get(url)

    data = response.json()
    meals = data['meals']
    selected_meals = []

    for meal in range(len(meals)):
        selected_meals.append(meals[meal])

    return render_template('menu.html', selected_meals=selected_meals, heading=heading, category_str=category_str)


@app.route('/choose/<category_str>')
def menu_choose(category_str):
    """Choose menu, with buttons and shopping_cart."""

    heading = "Choose your meals."
    session_cart = []
    id_cart = []
    response_cart = []
    session['cart_length'] = 0

    # SHOPPING CART API CALLS
    if 'cart_array' in session:
        # turn session string into a list of ids
        session_cart = session['cart_array'].lstrip(
            '["').rstrip('"]').split('","')
        id_cart = [eval(i) for i in session_cart]

        cart_length = len(id_cart)
        session['cart_length'] = cart_length

    for item_id in id_cart:
        item_url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={item_id}"

        item_response = requests.get(item_url)
        item_data = item_response.json()
        item = item_data['meals']
        response_cart.append(
            {
                "idMeal": eval(item[0]["idMeal"]),
                "strMeal": item[0]["strMeal"].title(),
                "strMealThumb": item[0]["strMealThumb"]
            }
        )

    print(response_cart)

    # MENU API CALLS
    menu_url = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category_str}"
    response = requests.get(menu_url)

    data = response.json()
    meals_json = data['meals']
    selected_meals = []

    for meal in range(len(meals_json)):
        selected_meals.append(meals_json[meal])

    # SESSION DATA
    session_plan_id = 1
    # set default plan
    if 'cart_plan_id' in session:
        session_plan_id = session['cart_plan_id']

    session_meal_cap = 3
    # set default cap
    if 'meal _cap' in session:
        session_meal_cap = session['meal _cap']

    return render_template('menu-choose.html', selected_meals=selected_meals, heading=heading, session_cart=session_cart, response_cart=response_cart, session_plan_id=session_plan_id, session_meal_cap=session_meal_cap)


@app.route("/cart", methods=["POST"])
def shopping_cart():
    """API for shopping_cart saving. Data sent from JS."""
    cart_array = []
    # pull the data sent from JS ajax post
    keys = request.form.keys()
    for key in keys:
        cart_array = key
    # should be able to do this without loop, as this is all data - not just cart array

    session['cart_array'] = cart_array

    return redirect(request.referrer)


@app.route("/cart/clear")
def cart_clear():
    """POST for clearing cart session."""

    if 'cart_array' in session:
        del session['cart_array']
        session['cart_length'] = 0

    return redirect(request.referrer)


@app.route("/checkout")
def checkout():
    """Deal with checkout, and database saving."""
    return render_template('checkout.html')


@app.route("/recipe/<int:meal_id>")
def profile_show_meal(meal_id):
    """Show recipe and ingredients for a given meal."""
    return render_template('recipe.html')


# ####################
# USERS
# ####################

@app.route("/profile")
def profile():
    """"""
    return render_template('profile.html')


@app.route("/profile/orders")
def profile_orders():
    return render_template('orders.html')


@app.route("/profile/edit")
def profile_edit():
    return render_template('edit.html')


@ app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # user = User.authenticate(form.username.data, form.password.data)

        # if user:
        #     session[CURR_USER_KEY] = user.id

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
