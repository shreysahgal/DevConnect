from flask_wtf import FlaskForm
from wtforms import StringField, TextField
from wtforms.validators import InputRequired

class CommentForm(FlaskForm):
    body = TextField('comment', validators=[InputRequired()])