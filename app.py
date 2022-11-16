import os

from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension

# from forms import UserAddForm, LoginForm, MessageForm, EditForm
from models import connect_db

CURR_USER_KEY = "curr_user"

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = (
#     os.environ.get('DATABASE_URL', 'postgresql:///warbler'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///prepkitchen'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")
toolbar = DebugToolbarExtension(app)

connect_db(app)


##############################################################################
# Homepage and error pages


@app.route('/')
def homepage():
    """Show homepage."""

    return render_template('index.html')


@app.route('/menu')
def show_menu():
    """Show menu preview."""
    return render_template('menu.html')


@app.route('/plans')
def show_plans():
    """Show plans page. Leads to ordering page."""

    return render_template('plans.html')

##############################################################################
# User signup/login/logout


# @app.before_request
# def add_user_to_g():
#     """If we're logged in, add curr user to Flask global."""

#     if CURR_USER_KEY in session:
#         g.user = User.query.get(session[CURR_USER_KEY])

#     else:
#         g.user = None


# def do_login(user):
#     """Log in user."""

#     session[CURR_USER_KEY] = user.id


# def do_logout():
#     """Logout user."""

#     if CURR_USER_KEY in session:
#         del session[CURR_USER_KEY]


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup."""

    return render_template('signup.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    return render_template('login.html')


@app.route('/logout')
def logout():
    """Handle logout of user."""

    # do_logout()
    flash(f"Goodbye! You have logged out.")
    return redirect("/")


##############################################################################
# General user routes:


@app.route('/users/<int:user_id>')
def users_show(user_id):
    """Show user profile."""

    # user = User.query.get_or_404(user_id)
    # check for user verification

    return render_template('profile.html')


@app.route('/users/delete', methods=["POST"])
def delete_user():
    """Delete user."""

    # db.session.delete(g.user)
    # db.session.commit()

    return redirect("/")


##############################################################################
# Turn off all caching in Flask
#   (useful for dev; in production, this kind of stuff is typically
#   handled elsewhere)
#
# https://stackoverflow.com/questions/34066804/disabling-caching-in-flask

# @ app.after_request
# def add_header(req):
#     """Add non-caching headers on every request."""

#     req.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     req.headers["Pragma"] = "no-cache"
#     req.headers["Expires"] = "0"
#     req.headers['Cache-Control'] = 'public, max-age=0'
#     return req
