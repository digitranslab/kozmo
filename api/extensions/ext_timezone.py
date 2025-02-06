import os
import time

from kozmo_app import KozmoApp


def init_app(app: KozmoApp):
    os.environ["TZ"] = "UTC"
    # windows platform not support tzset
    if hasattr(time, "tzset"):
        time.tzset()
