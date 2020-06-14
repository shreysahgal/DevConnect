from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

from devconnect.models import User, Post, Tag, Comment, db
from config import Config
from devconnect.fake import users, posts, comments
from sqlalchemy.exc import IntegrityError


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


def add_admin():
    admin = User(
        email = 'admin@gmail.com',
        username = 'admin',
        password = generate_password_hash('password', method='SHA256'),
        tags = [t for t in Tag.query.all()]
    )
    db.session.add(admin)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()

def add_tags():
    print('hi)')
    p = Tag(name='Programmer')
    d = Tag(name='Designer')
    e = Tag(name='Entrepreneur')

    try:
        db.session.add_all([p, d, e])
        db.session.commit()
    except IntegrityError:
        db.session.rollback()

# # comment out when not reinstantiating the databases
# with app.app_context():

#     db.create_all()
#     db.create_all()
    
#     add_admin()
#     add_tags()

#     users(50)
#     posts(50)
#     comments(50)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
Bootstrap(app)

from devconnect.auth import bp as auth_bp
app.register_blueprint(auth_bp)

from devconnect.home import bp as home_bp
app.register_blueprint(home_bp)

from devconnect.profile import bp as profile_bp
app.register_blueprint(profile_bp)

from devconnect.view_post import bp as view_post_bp
app.register_blueprint(view_post_bp)

from devconnect.create_post import bp as create_post_bp
app.register_blueprint(create_post_bp)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True)