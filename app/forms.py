from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField

class LoginForm(Form):
    username = StringField('User name', [
        validators.length(min=4, max=50, message='El username esta fuera del rango')
    ])
    password = PasswordField('Password', [
        validators.Required()
    ])