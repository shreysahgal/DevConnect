from flask import Blueprint

bp = Blueprint('home', __name__, template_folder="templates", static_folder="static", static_url_path="/home/static")

from devconnect.home import routes