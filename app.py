from flask import Flask, render_template, redirect
import requests
from models import connect_db, db, User
# from forms import NewSongForPlaylistForm, SongForm, PlaylistForm
# from sqlalchemy.exc import IntegrityError
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True

connect_db(app)
# db.create_all()


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

    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=Seafood"
    response = requests.get(url)

    data = response.json()
    meals = data['meals']
    selected_meals = []

    for meal in range(len(meals)):
        selected_meals.append(meals[meal])

    return render_template('menu-choose.html', selected_meals=selected_meals, heading=heading)


@app.route('/choose/post', methods=['POST'])
def menu_choose_post():

    heading = "Choose your meals."

    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=Seafood"
    response = requests.get(url)

    data = response.json()
    meals = data['meals']
    selected_meals = []

    for meal in range(len(meals)):
        selected_meals.append(meals[meal])

    return redirect('/choose')


# USERS

@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup.
    Create new user and add to DB. Redirect to home page.
    If form not valid, present form.
    If the there already is a user with that username: flash message
    and re-present form.
    """

    form = UserAddForm()

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
            db.session.commit()

        except IntegrityError:
            flash("Username already taken", 'danger')
            return render_template('users/signup.html', form=form)

        do_login(user)

        return redirect("/")

    else:
        return render_template('users/signup.html', form=form)
