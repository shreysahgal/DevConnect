from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, RadioField
from wtforms.validators import InputRequired, Email, Length


class PostForm(FlaskForm):
    kind = RadioField('kind', choices = [('i','Idea'),('qa','Q&A'),('u', 'Update')], validators=[InputRequired()])
    title = StringField('title', validators=[InputRequired()])
    descrip = StringField('descrip', validators=[InputRequired(), Length(min=10, max=80)])