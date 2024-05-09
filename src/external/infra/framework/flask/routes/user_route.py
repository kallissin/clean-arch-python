from flask import Blueprint, request, jsonify
from src.adapter.request import request_adapter
from src.external.composers.user_finder_composer import user_finder_composer
from src.external.composers.user_register_composer import user_register_composer


user_route_bp = Blueprint("user_routes", __name__)

@user_route_bp.route("/v1/user/find", methods=["GET"])
def find_user():
    http_response = request_adapter(request, user_finder_composer())

    return jsonify(http_response.body, http_response.status_code)


@user_route_bp.route("/v1/user", methods=["POST"])
def register_user():
    http_response = request_adapter(request, user_register_composer())

    return jsonify(http_response.body, http_response.status_code)
