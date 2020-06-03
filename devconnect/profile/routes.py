from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy

# from devconnect.profile.forms import EditProfileForm
from devconnect.models import User
from devconnect.profile import bp
from config import Config


@bp.route('/user/<username>')
def view_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    if user:
        is_a = ' & '.join([t.name for t in user.tags])
        return render_template('displayuser.html', user=user, is_a=is_a)
    return "user doesn't exist"
