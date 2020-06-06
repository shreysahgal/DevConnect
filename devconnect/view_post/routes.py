from flask import Flask, render_template, redirect, Markup
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, login_user, logout_user, current_user

from devconnect.models import Post, Comment, db
from config import Config
from devconnect.view_post import bp
from devconnect.view_post.forms import CommentForm

@bp.route('/post/<postid>', methods=['GET', 'POST'])
@login_required
def view_post(postid):
    form = CommentForm()

    if form.validate_on_submit():
        new_comment = Comment(
            body=form.body.data,
            author=current_user,
            post=Post.query.get(postid)
        )

        db.session.add(new_comment)
        db.session.commit()

        return redirect('/post/'+postid)

    post = Post.query.get(postid)
    return render_template('post.html', post=post, form=form, Markup=Markup)
