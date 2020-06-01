from flask import Blueprint

bp = Blueprint('auth', __name__)

from devconnect.auth import routes