
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', 
        validators=[DataRequired(), Length(min=5)])
    password =PasswordField('Password',
        validators=[DataRequired(), Length(min=5)])
    submit = SubmitField('Login')
