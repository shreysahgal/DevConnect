from flask import Flask, render_template, request, redirect, url_for, flash, Markup
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user

from devconnect import User, Post
from devconnect.profile import bp
from devconnect.profile.forms import EditProfileForm, FollowForm
from devconnect import db
from config import Config


@bp.route('/user/<username>')
def view_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    if user:
        is_a = ' & '.join([t.name for t in user.tags])
        posts = Post.query.filter(Post.author == user)   
        followForm = FollowForm()
        return render_template('displayuser.html', user=user, is_a=is_a, posts=posts, followForm=followForm, Markup=Markup)
    return "user doesn't exist"


@bp.route('/edit_profile', methods=['GET', 'POST'])
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

@bp.route('/follow/<username>', methods =['POST']) 
@login_required
def follow(username): 
    form = FollowForm() 
    if form.validate_on_submit(): 
        user = User.query.filter_by(username=username).first() 
        if user is None: 
            flash('User {} not found.'.format(username))
            return redirect(url_for('home.index'))
        if user == current_user:
            flash('You cannot follow yourself narcissist -.-')
            return redirect(url_for('profile.view_user', username=current_user.username))
        current_user.follow(user)
        db.session.commit()
        flash('You are following {}!'.format(username))
        return redirect(url_for('profile.view_user', username=user.username))
    else: 
        return redirect(url_for('home.index')) #if somehow CSRF token fails
        
@bp.route('/unfollow/<username>', methods =['POST']) 
@login_required
def unfollow(username): 
    form = FollowForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first() 
        if user is None: 
            flash("User {} not found.".format(username))
            return redirect(url_for('home.index'))
        if user == current_user: 
            flash("You cannot unfollow yourself scrub".format(username))
            return redirect(url_for('profile.view_user', username=current_user.username))
        current_user.unfollow(user)
        db.session.commit()
        flash('You are not following {} sucks for them i guess'.format(username))
        return redirect(url_for('profile.view_user', username=user.username))
    else:
        return redirect(url_for('home.index')) #if somehow CSRF token fails
