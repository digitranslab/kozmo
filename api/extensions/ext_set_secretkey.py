from configs import kozmo_config
from kozmo_app import KozmoApp


def init_app(app: KozmoApp):
    app.secret_key = kozmo_config.SECRET_KEY
