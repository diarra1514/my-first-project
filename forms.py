from flask_wtf import FlaskForm
from wtforms import stringField, PasswordField, submitField, BooleanField
from wtforms.validators import DataRequired,length,Email, EqualTo



class RegistrationForm(FlaskForm):
    username = stringField('username', 
                            validators=[DataRequired(),length(min=2,max=20)])
    email= stringField('Email', 
                        validators=[DataRequired(), Email()])

    password  = passwordField('password', validators=[DataRequired()])
    confirm_password  = passwordField('confirm password', 
                                                validators=[DataRequired(), EqualTo('password')])
submit = submitField('sign Up')




class LoginForm(FlaskForm):
   email= stringField('Email', 
                        validators=[DataRequired(), Email()])

    password  = passwordField('password', validators=[DataRequired()])
    
     remember = BooleanField('Remember Me')
    submit = submitField('Login')