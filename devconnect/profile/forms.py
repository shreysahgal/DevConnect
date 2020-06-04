from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length

class EditProfileForm(FlaskForm): 
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])