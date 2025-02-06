from configs import kozmo_config
from kozmo_app import KozmoApp


def is_enabled() -> bool:
    return kozmo_config.API_COMPRESSION_ENABLED


def init_app(app: KozmoApp):
    from flask_compress import Compress  # type: ignore

    compress = Compress()
    compress.init_app(app)
