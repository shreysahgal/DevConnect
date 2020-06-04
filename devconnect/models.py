import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

assoc_table = db.Table('assoc',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    kind = db.Column(db.String())
    author = db.Column(db.String(15))
    title = db.Column(db.String(25))
    descrip = db.Column(db.String())

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', secondary=assoc_table, backref=db.backref('tags', lazy='dynamic'), lazy='dynamic')

if __name__ == '__main__':
    user = User(email="email", username="username", password="password")