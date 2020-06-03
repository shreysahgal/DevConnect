from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, login_user, logout_user, current_user

from devconnect.models import Post
from config import Config
from devconnect.view_post import bp

@bp.route('/post/<postid>')
@login_required
def view_post(postid):
    post = Post.query.filter_by(id=postid).first_or_404()
    return render_template('post.html', post=post)
