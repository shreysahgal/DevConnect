from flask import render_template

from devconnect.home import bp
from devconnect.models import User, Post


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
    if (typefilter == ""):
        posts = Post.query.order_by('created')
    else:
        posts = Post.query.filter(
            Post.kind == typefilter).order_by('created')
    response = {"posts": []}
    serialized_posts = response["posts"]
    for p in posts.limit(10).all():
        serialized_posts.append(p.serialize())
    return response


@bp.route('/search/<searchterms>')
def search(searchterms):
    # for now, just search for anything that exactly matches the search terms, but eventually
    # terms were separated by commas in javascript, so we separate them here
    terms = searchterms.split(",")
    print(terms)
    # get users
    users = User.query.filter(
        User.username.in_(terms)).order_by('created').limit(10).all()
    # get posts
    posts = Post.query.filter(
        Post.title.in_(terms)).order_by('created').limit(10).all()
    return render_template("search.html", users=users, posts=posts)
