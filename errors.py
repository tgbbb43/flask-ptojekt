from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity
from flask import jsonify, Blueprint

error_bp = Blueprint("errors", __name__)

@error_bp.app_errorhandler(NotFound)
def handle_not_found(e):
    return jsonify({
        "error": "Not Found",
        "message": str(e.description)
    }), 404

@error_bp.app_errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify({
        "error": "Bad Request",
        "message": str(e.description)
    }), 400

@error_bp.app_errorhandler(UnprocessableEntity)
def handle_unprocessable_entity(e):
    return jsonify({
        "error": "Unprocessable Entity",
        "message": str(e.description)
    }), 422

@error_bp.app_errorhandler(Conflict)
def handle_conflict(e):
    return jsonify({
        "error": "Conflict",
        "message": str(e.description)
    }), 409