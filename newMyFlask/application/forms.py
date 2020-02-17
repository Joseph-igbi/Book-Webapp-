
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users



class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators = [DataRequired(), Length(min=2, max=30)])
    last_name = StringField('Last Name', validators = [DataRequired(), Length(min=2, max=40)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), ])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Sign up')
    def validate_email(self, email):
        user = Users.query.filter_by(email= email.data).first()

        if user:
            raise ValidationError('Email already in use')





class LoginForm(FlaskForm):
    email = StringField('Email', validators =[DataRequired(),Email()])

    password = PasswordField('Password', validators = [DataRequired()])
    
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class SearchForm(FlaskForm):
    
    search=StringField('search', validators =[DataRequired()])
    submit = SubmitField('Search')


    
