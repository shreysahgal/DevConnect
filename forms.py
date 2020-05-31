from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, RadioField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = StringField('password', validators=[InputRequired(), Length(min=10, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = StringField('password', validators=[InputRequired(), Length(min=10, max=80)])
    programmer = BooleanField('programmer')
    designer = BooleanField('designer')
    entrepreneur = BooleanField('entrepreneur')

class PostForm(FlaskForm):
    kind = RadioField('kind', choices = [('i','Idea'),('qa','Q&A'),('u', 'Update')], validators=[InputRequired()])
    title = StringField('title', validators=[InputRequired()])
    descrip = StringField('descrip', validators=[InputRequired(), Length(min=10, max=80)])

class EditProfileForm(FlaskForm): 
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])