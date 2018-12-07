from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,PasswordField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from main.models import User,BusinessClass

class Registration(FlaskForm):
    firstName=StringField('First Name',validators=[DataRequired(),Length(max=30)])
    middleName=StringField('Middle Name',validators=[DataRequired(),Length(max=30)])
    lastName=StringField('Last Name',validators=[DataRequired(),Length(max=30)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirmPassWord=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That Email is taken.Please choose another one')

class Login(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remeber Me')
    submit=SubmitField('Login')

    # def validate_forms(self,emial):
    #     if True:
    #         User=User.query.filter_by(email=email.data).first()
    #         raise ValidationError('Validation Message')

class BusinessForm(FlaskForm):
    projectName=StringField('Project Name',validators=[DataRequired(),Length(max=30)])
    projectTags=StringField('Tags',validators=[DataRequired(),Length(max=30)])
    lastName=StringField('Last Name',validators=[DataRequired(),Length(max=30)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirmPassWord=PasswordField('Email',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Submit')

    # def validate_forms(self,field):
    #     if True:
    #         raise ValidationError('Validation Message')

class resetForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    submit=SubmitField('Reset')
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account by that email')

class resetPassword(FlaskForm):
    password=PasswordField('Password',validators=[DataRequired()])
    confirmPassWord=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Reset Password')