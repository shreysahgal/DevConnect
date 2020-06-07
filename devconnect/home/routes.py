from flask import Flask, render_template, jsonify, request

from sqlalchemy.sql import text

from devconnect.home import bp
from devconnect.models import Post
from config import Config

import json

# maybe this can even route to /filter/, since with no facet it just does 10 recent results
@bp.route('/')
@bp.route('/home/')
def index():
    # get 10 most recent posts
    posts = Post.query.order_by('created').limit(10)
    return render_template('index.html', posts=posts)

# use this: https://www.geeksforgeeks.org/append-to-json-file-using-python/
@bp.route('/filter/', methods=['POST'])
@bp.route('/filter/<facet>', methods=['POST'])
def filter(facet=""):
    if (facet == ""):
        posts = Post.query.order_by('created').limit(10)
    else:
        posts = Post.query.filter(
            Post.kind == facet).order_by('created').limit(10)
    response = {"posts": []}
    serialized_posts = response["posts"]
    for p in posts.all():
        serialized_posts.append(p.serialize())
    return response
