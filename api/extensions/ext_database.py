from kozmo_app import KozmoApp
from models import db


def init_app(app: KozmoApp):
    db.init_app(app)
