from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
	"""docstring for SignupForm"""
	first_name = StringField('First name', validators=[DataRequired('Please enter your first name')])
	last_name = StringField('Last name', validators=[DataRequired('Please enter your last name')])
	email = StringField('Email', validators=[DataRequired('Please enter your email'), Email('Invalid Email')])
	password = PasswordField('Password', validators=[DataRequired('Please enter your password'), Length(min=6, message="Password must be 6 characters") ])
	submit = SubmitField('Sign up')	

class LoginForm(Form):
	"""docstring for LoginForm"""
	email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter mail in valid format")])
	password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
	submit = SubmitField("Sign In")

class AddressForm(Form):
	address = StringField('Address', validators=[DataRequired("Please enter an address")])
	submit = SubmitField("Search")