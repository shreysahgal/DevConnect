import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

assoc_table = db.Table('assoc',
                       db.Column('user_id', db.Integer,
                                 db.ForeignKey('users.id')),
                       db.Column('tag_id', db.Integer,
                                 db.ForeignKey('tags.id'))
                       )


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

    # implicit "tags" field here because of many-to-many relationship
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    kind = db.Column(db.String())
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(25))
    descrip = db.Column(db.String())
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    def serialize(self):
        return {
            'id': self.id,
            'created': self.created.strftime("%m/%d/%Y, %H:%M:%S"),
            'kind': self.kind,
            'author': self.author.username,
            'title': self.title,
            'descrip': self.descrip
        }


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', secondary=assoc_table, backref=db.backref(
        'tags', lazy='dynamic'), lazy='dynamic')


if __name__ == '__main__':
    user = User(email="email", username="username", password="password")
