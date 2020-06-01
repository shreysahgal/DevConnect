import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

userdb = SQLAlchemy()
postdb = SQLAlchemy()

class User(UserMixin, userdb.Model):
    id = userdb.Column(userdb.Integer, primary_key=True)
    created = postdb.Column(postdb.DateTime, default=datetime.datetime.utcnow)
    username = userdb.Column(userdb.String(15), unique=True)
    email = userdb.Column(userdb.String(50), unique=True)
    password = userdb.Column(userdb.String(80))
    tags = userdb.Column(userdb.String(3)) # programmer/designer/entrepreneur

class Post(postdb.Model):
    id = postdb.Column(postdb.Integer, primary_key=True)
    created = postdb.Column(postdb.DateTime, default=datetime.datetime.utcnow)
    kind = postdb.Column(postdb.String())
    author = postdb.Column(postdb.String(15))
    title = postdb.Column(postdb.String(25))
    descrip = postdb.Column(postdb.String())


if __name__ == '__main__':
    user = User(email="email", username="username", password="password")