from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField
from wtforms.validators import InputRequired

STATE_ABBREV = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
                'HI', 'ID', 'IL', 'IN', 'IO', 'KS', 'KY', 'LA', 'ME', 'MD',
                'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
                'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
                'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
STATE_LIST = [(state, state) for state in STATE_ABBREV]


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    first_name = StringField("First Name", validators=[InputRequired()])
    last_name = StringField("Last Name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired()])
    address_street = StringField("Address", validators=[InputRequired()])
    address_city = StringField("City", validators=[InputRequired()])
    address_state = SelectField(
        "State", choices=STATE_LIST)
    address_zip = StringField("ZIP", validators=[InputRequired()])


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])


class CheckoutForm(FlaskForm):
    billing_name = StringField("Name on card", validators=[InputRequired()])
    billing_card = StringField("Card number", validators=[InputRequired()])
    billing_code = StringField(
        "Security code", validators=[InputRequired()])
    billing_street = StringField(
        "Billing Address", validators=[InputRequired()])
    billing_city = StringField("City", validators=[InputRequired()])
    billing_state = SelectField(
        "State", choices=STATE_LIST)
    billing_zip = StringField("ZIP", validators=[InputRequired()])
