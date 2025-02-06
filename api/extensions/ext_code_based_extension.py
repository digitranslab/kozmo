from core.extension.extension import Extension
from kozmo_app import KozmoApp


def init_app(app: KozmoApp):
    code_based_extension.init()


code_based_extension = Extension()
