from random import randint, sample
from sqlalchemy.exc import IntegrityError
from faker import Faker
from devconnect.models import User, Post, Tag, Comment, db

def users(count=20):
    fake = Faker()
    i = 0

    while i < count:
     
        tags = sample([t for t in Tag.query.all()], k=randint(1,3))

        u = User(
            email=fake.email(),
            username=fake.user_name(),
            password='password',
            tags=tags
        )
        db.session.add(u)

        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()

def posts(count=20):
    fake = Faker()
    user_count = User.query.count()

    for i in range(count):
        u = User.query.get(randint(1, user_count-1))
        kind = ['Idea', 'Q&A', 'Update'][randint(0,2)]
        title = ' '.join(fake.words())
        descrip = ' '.join(fake.sentences())
        p = Post(
            kind=kind,
            author=u,
            title=title,
            descrip=descrip
        )
        db.session.add(p)
    db.session.commit()

def comments(count=20):
    fake = Faker()
    user_count = User.query.count()
    post_count = Post.query.count()

    for i in range(count):
        u = User.query.get(randint(1, user_count-1))
        p = Post.query.get(randint(1, post_count-1))
        body = fake.sentence()
        c = Comment(body=body, author=u, post=p)
        db.session.add(c)
    db.session.commit()
        