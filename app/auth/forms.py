from flask_wtf import FlaskForm
from wtforms import Form,StringField, TextAreaField, SubmitField, BooleanField,PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name: ', validators=[DataRequired()])
    
    last_name = StringField('Last Name: ', validators=[DataRequired()])
    
    username = StringField('Username: ', validators=[DataRequired()])
    
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    
    password = PasswordField('Password: ', validators=[DataRequired()])
    
    confirm_password = PasswordField('Confirm Password: ', validators=[DataRequired(),EqualTo('password')])
    
    submit = SubmitField('Sign Up')
    
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
    
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LogInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    
    password = PasswordField('Password', validators=[DataRequired()])
    
    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Sign In')
    