from flask import Flask, render_template, request, Markup

from devconnect.home import bp
from devconnect.models import Post, db, Comment, User
from config import Config

@bp.route('/')
@bp.route('/home')
def index():
    page = request.args.get('page',1, type=int)
    pagination = Post.query.order_by('created').paginate(page, per_page=10, error_out=False)
    posts = pagination.items
    return render_template('index.html', posts=posts, pagination=pagination, Markup=Markup)
