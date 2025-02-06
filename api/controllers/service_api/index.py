from flask_restful import Resource  # type: ignore

from configs import kozmo_config
from controllers.service_api import api


class IndexApi(Resource):
    def get(self):
        return {
            "welcome": "Kozmo OpenAPI",
            "api_version": "v1",
            "server_version": kozmo_config.CURRENT_VERSION,
        }


api.add_resource(IndexApi, "/")
