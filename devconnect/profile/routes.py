from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy

# from devconnect.profile.forms import EditProfileForm
from devconnect.models import User, userdb
from devconnect.profile import bp
from config import Config

def decode_tags(tagstr):
    taglist = list()
    for t in tagstr:
        if t == 'P':
            taglist.append('Programmer')
        elif t == 'D':
            taglist.append('Designer')
        elif t == 'E':
            taglist.append('Entrepreneur')
    return taglist

@bp.route('/user/<username>')
def view_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    if user:
        is_a = ' & '.join(decode_tags(user.tags))
        return render_template('displayuser.html', user=user, is_a=is_a)
    return "user doesn't exist"
