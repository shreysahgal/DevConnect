from flask import Blueprint

bp = Blueprint('create_post', __name__, template_folder="templates", static_folder="static", static_url_path="/create_post/static")

from devconnect.create_post import routes