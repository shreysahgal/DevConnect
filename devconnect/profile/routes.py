from flask import Flask, render_template, request, redirect, url_for, Markup
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user

# from devconnect.profile.forms import EditProfileForm
from devconnect import User, Post
from devconnect.profile import bp
from devconnect.profile.forms import EditProfileForm
from devconnect import db
from config import Config


@bp.route('/user/<username>')
def view_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    if user:
        is_a = ' & '.join([t.name for t in user.tags])
        posts = Post.query.filter(Post.author == user)   
        isLoggedin = user == current_user
        return render_template('displayuser.html', user=user, is_a=is_a, posts=posts, edit=isLoggedin, Markup=Markup)
    return "user doesn't exist"

@bp.route('/edit_profile', methods = ['GET', 'POST'])
@login_required
def edit_profile(): 
    form = EditProfileForm()
    if form.validate_on_submit(): 
        current_user.username = form.username.data
        db.session.commit() 
        return redirect(url_for('profile.view_user', username=current_user.username))
    elif request.method == 'GET':
        form.username.data = current_user.username
    return render_template('edit_profile.html', form=form)