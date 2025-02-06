from configs import kozmo_config
from kozmo_app import KozmoApp


def init_app(app: KozmoApp):
    if kozmo_config.RESPECT_XFORWARD_HEADERS_ENABLED:
        from werkzeug.middleware.proxy_fix import ProxyFix

        app.wsgi_app = ProxyFix(app.wsgi_app)  # type: ignore
