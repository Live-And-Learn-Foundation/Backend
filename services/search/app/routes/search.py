from flask import Blueprint, jsonify, request
from flask import Blueprint, jsonify
from app.controllers import SearchController

search_blueprint = Blueprint("search_engine", __name__,
                             url_prefix="/api/v1/search")


@search_blueprint.route("/", methods=["GET"])
def search():
    query = request.args.get("query", "")
    search_results = SearchController().get(query=query)

    return jsonify(search_results)
