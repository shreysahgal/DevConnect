from flask import Blueprint

bp = Blueprint('profile', __name__, template_folder="templates", static_folder="static", static_url_path="/profile/static")

from devconnect.profile import routes