from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                                Length, EqualTo)

from models import User

def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('User with that user already exists.')

class RegisterForm(Form):
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(),
            email_exists
            ])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6),
            EqualTo('password2', message='Passwords must match')
            ])
    password2 = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired()
            ]
    )
    
class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    
class TacoForm(Form):
    protein = StringField(
      "Taco protein", 
      validators=[DataRequired(),
                  Regexp(
                         r'^[-a-zA-Z\s]+$',
                         message = "Letters, spaces, and hyphens only."
        )])
    shell = StringField(
      "Taco shell",
      validators=[DataRequired(),
                  Regexp(
                        r'^[a-zA-Z\s-]+$',
                        message = "Letters, spaces, and hyphens only."
        )])
    cheese = BooleanField(
      "Cheese?")
    extras = TextAreaField(
      "Extras")
            
