from kozmo_app import KozmoApp


def init_app(app: KozmoApp):
    import flask_migrate  # type: ignore

    from extensions.ext_database import db

    flask_migrate.Migrate(app, db)
