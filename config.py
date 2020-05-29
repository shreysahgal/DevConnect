from os import path

ROOT = path.abspath(path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(ROOT, 'users.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'VeRySeCrEt;)'