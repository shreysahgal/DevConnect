from flask import Flask, render_template

from devconnect.home import bp
from devconnect.models import Post
from config import Config

@bp.route('/')
@bp.route('/home')
def index():
    posts = Post.query.order_by('created').limit(10) # get 10 most recent posts
    return render_template('index.html', posts=posts)
