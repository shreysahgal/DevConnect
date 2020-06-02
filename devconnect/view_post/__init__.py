from flask import Blueprint

bp = Blueprint('view_post', __name__, template_folder="templates", static_folder="static", static_url_path="/view_post/static")

from devconnect.view_post import routes