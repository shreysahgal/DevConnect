from flask_wtf import FlaskForm
from wtforms import StringField, TextField, IntegerField, SubmitField
from wtforms.validators import InputRequired

class CommentForm(FlaskForm):
    body = TextField('', validators=[InputRequired()])
    submit = SubmitField('comment')

class ReplyForm(FlaskForm):
    parentid = IntegerField('parent', validators=[InputRequired()])
    body = TextField('', validators=[InputRequired()])
    submit = SubmitField('reply')
