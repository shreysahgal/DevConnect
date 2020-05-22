import time
from flask_bcrypt import generate_password_hash
from flask_login import UserMixin
from peewee import *

DATABASE = SqliteDatabase('social.db')

class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=30)
    joined_at = DateTimeField(default=time.time())

    class Meta:
        database = DATABASE
        order_by = ('-join_at',)
        
    @classmethod
    def create_user(cls, username, email, password):
        try:
            cls.create(
                username = username,
                email=email,
                password=generate_password_hash(password))
        except IntegrityError:
            raise ValueError("User already exists.")
    
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()