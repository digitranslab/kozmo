from kozmo_app import KozmoApp


def init_app(app: KozmoApp):
    from events import event_handlers  # noqa: F401
