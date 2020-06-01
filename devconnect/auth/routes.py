from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required,login_user, logout_user, current_user

from devconnect.auth import bp
from devconnect.auth.forms import LoginForm, RegisterForm
from devconnect.models import User, userdb
from devconnect import userdb
from config import Config

def encode_tags(p, d, e):
    tagstr = 'P'*p + 'D'*d + 'E'*e
    return tagstr

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect('/home')
        return "wrong again bitch"
        # return "<p>%s</p><p>%s</p>" % (form.username.data, form.password.data)
    return render_template('login.html', form=form)

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_pass = generate_password_hash(form.password.data, method="sha256")
        tagstr = encode_tags(form.programmer.data, form.designer.data, form.entrepreneur.data)
        new_user = User(
            email = form.email.data,
            username = form.username.data,
            password = hashed_pass,
            tags = tagstr)
        userdb.session.add(new_user)
        userdb.session.commit()
        return redirect('/login')
        # return  "<p>%s</p><p>%s</p><p>%s</p>" % (form.email.data, form.username.data, form.password.data)
    return render_template('signup.html', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')