from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user
from slugify import slugify

from devconnect.models import Post, db
from devconnect.create_post import bp
from devconnect.create_post.forms import PostForm
from config import Config


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()

    if form.validate_on_submit():
        kind = form.kind.data
        title = form.title.data
        descrip = form.descrip.data
        slug = slugify(form.title.data)
        new_post = Post(
            kind=kind,
            author=current_user,
            title=title,
            descrip=descrip, 
            slug=slug
        )
        db.session.add(new_post)
        db.session.commit() 
        flash("post created")
        return redirect('/')
    return render_template('create.html', form=form)
