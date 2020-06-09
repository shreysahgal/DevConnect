from flask import Flask, render_template, jsonify, request

from sqlalchemy.sql import text

from devconnect.home import bp
from devconnect.models import User, Post
from config import Config

import json

# maybe this can even route to /filter/, since with no facet it just does 10 recent results


@bp.route('/')
@bp.route('/home/')
def index():
    # get 10 most recent posts
    posts = Post.query.order_by('created').limit(10)
    return render_template('index.html', posts=posts)

# facets are done in specific order (hard coded)
# 1. type, 2. author


@bp.route('/filter/', methods=['POST'])
@bp.route('/filter/<facets>', methods=['POST'])
def filter(facets=""):
    filters = facets.split(",")
    typefilter = filters[0]
    authorfilter = filters[1]
    # get user id with this name (not sure if necessary, but couldnt find a workaround, maybe im big dumb)
    # also seems VERY dangerous to directly get id on same call as query but oh well we live life on the edge
    author = User.query.filter(User.username == authorfilter).limit(1)
    if author.count() > 0:
        authorid = author[0].id
    else:
        authorid = ""
    if (typefilter == ""):
        posts = Post.query.order_by('created')
    else:
        posts = Post.query.filter(
            Post.kind == typefilter).order_by('created')
    if (authorid != ""):
        posts = posts.filter(
            Post.author_id == authorid).order_by('created')
    response = {"posts": []}
    serialized_posts = response["posts"]
    for p in posts.limit(10).all():
        serialized_posts.append(p.serialize())
    return response
