from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length

class EditProfileForm(FlaskForm): 
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])

#this is an empty form for following people (we don't want people to actually submit a form)
class FollowForm(FlaskForm): 
    submit = SubmitField('submit')
