from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user

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
        author = current_user.username
        title = form.title.data
        descrip = form.descrip.data
        new_post = Post(
            kind=kind,
            author=author,
            title=title,
            descrip=descrip
        )
        db.session.add(new_post)
        db.session.commit()
        return "post created"
    return render_template('create.html', form=form)
