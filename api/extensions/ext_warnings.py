from kozmo_app import KozmoApp


def init_app(app: KozmoApp):
    import warnings

    warnings.simplefilter("ignore", ResourceWarning)
