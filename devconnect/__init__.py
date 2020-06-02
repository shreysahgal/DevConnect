from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

from devconnect.models import User, Post, userdb, postdb
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
userdb.init_app(app)
postdb.init_app(app)


# comment out when not reinstantiating the databases
with app.app_context():
    userdb.create_all()
    postdb.create_all()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
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