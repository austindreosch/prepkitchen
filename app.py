from flask import Flask, render_template
from models import connect_db
import requests

from flask import Flask, render_template

# from forms import UserAddForm, LoginForm, MessageForm, EditForm

# CURR_USER_KEY = "curr_user"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///prepkitchen'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
# db.create_all()


##############################################################################
# Homepage and error pages


@app.route('/')
def homepage():
    """Show homepage."""

    return render_template('index.html')


@app.route('/menu')
def show_menu():
    """Show menu preview."""
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=Seafood"
    response = requests.get(url)

    data = response.json()
    meals = data['meals']
    selected_meals = []

    for meal in range(len(meals)):
        selected_meals.append(meals[meal])

    return render_template('menu.html', selected_meals=selected_meals)


@app.route('/plans')
def show_plans():
    """Show plans page. Leads to ordering page."""

    return render_template('plans.html')
