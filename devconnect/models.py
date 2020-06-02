import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    tags = db.Column(db.String(3)) # programmer/designer/entrepreneur

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    kind = db.Column(db.String())
    author = db.Column(db.String(15))
    title = db.Column(db.String(25))
    descrip = db.Column(db.String())


if __name__ == '__main__':
    user = User(email="email", username="username", password="password")