from core.hosting_configuration import HostingConfiguration

hosting_configuration = HostingConfiguration()


from kozmo_app import KozmoApp


def init_app(app: KozmoApp):
    hosting_configuration.init_app(app)
