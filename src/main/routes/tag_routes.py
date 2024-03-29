from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView

from src.erros.error_handler import hander_errors

from src.validators.tag_creator_validator import tag_creator_validator

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=["POST"])  # Add ".route" after "@tags_routes_bp" and a colon at the end
def create_tags():
    response = None
    try:
        tag_creator_validator(request)
        tag_creator_view = TagCreatorView()

        http_request = HttpRequest(body=request.json)
        response = tag_creator_view.validate_and_create(http_request)
    except Exception as exeption:
        response = hander_errors(exeption)


    return jsonify(response.body), response.status_code