from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

from devconnect.forms import PostForm
from devconnect.models import User, Post, userdb, postdb
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
userdb.init_app(app)
postdb.init_app(app)


# comment out when not reinstantiating the databases
# with app.app_context():
#     userdb.create_all()
#     postdb.create_all()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
Bootstrap(app)

from devconnect.auth import bp as auth_bp
app.register_blueprint(auth_bp)

def decode_tags(tagstr):
    taglist = list()
    for t in tagstr:
        if t == 'P':
            taglist.append('Programmer')
        elif t == 'D':
            taglist.append('Designer')
        elif t == 'E':
            taglist.append('Entrepreneur')
    return taglist

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    # need to list posts
    # TODO: personalize for user
    posts = Post.query.order_by('created').limit(10) # get 10 most recent posts
    return render_template('home.html', posts=posts)

@app.route('/user/<username>')
def view_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    if user:
        is_a = ' & '.join(decode_tags(user.tags))
        return render_template('displayuser.html', user=user, is_a=is_a)
    return "user doesn't exist"

@app.route('/post/<postid>')
@login_required
def view_post(postid):
    post = Post.query.filter_by(id=postid).first_or_404()
    return render_template('post.html', post=post)


@app.route('/create', methods=['GET', 'POST'])
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
        postdb.session.add(new_post)
        postdb.session.commit()
        return "post created"
    return render_template('create.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)