from flask import Flask, render_template

from devconnect.home import bp
from devconnect.models import Post, db, Comment, User
from config import Config

@bp.route('/')
@bp.route('/home')
def index():

    # TODO: delete this shit lmao
    
    # p = Post.query.get(1)
    # # u = User.query.get(1)
    # # papa_comment = Comment(body="im a comment !", author=u, post=p, parent=None)
    # u = User.query.get(2)
    # c = Comment.query.get(1)

    # subcom = Comment(body="ur idiot", author=u, post=p, parent=c)

    # db.session.add(subcom)
    # db.session.commit()

    
    posts = Post.query.order_by('created').limit(10) # get 10 most recent posts
    return render_template('index.html', posts=posts)