import json

from . import main_blueprint


@main_blueprint.after_request
def after_request(response):
    header = response.headers
    header["Content-Type"] = "application/json"
    return response


@main_blueprint.route("/", methods=["GET"])
def shop_backend() -> str:
    return json.dumps({"message": "hola"}), 200
