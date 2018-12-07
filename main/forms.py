from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class Registration(FlaskForm):
    firstName=StringField('First Name',validators=[DataRequired(),Length(max=30)])
    middleName=StringField('Middle Name',validators=[DataRequired(),Length(max=30)])
    lastName=StringField('Last Name',validators=[DataRequired(),Length(max=30)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=StringField('Password',validators=[DataRequired()])
    confirmPassWord=StringField('Email',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')

class Login(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=StringField('Password',validators=[DataRequired()])
    remember=BooleanField('Remeber Me')
    submit=SubmitField('Login')

class BusinessForm(FlaskForm):
    projectName=StringField('Project Name',validators=[DataRequired(),Length(max=30)])
    projectTags=StringField('Tags',validators=[DataRequired(),Length(max=30)])
    lastName=StringField('Last Name',validators=[DataRequired(),Length(max=30)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=StringField('Password',validators=[DataRequired()])
    confirmPassWord=StringField('Email',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Submit')