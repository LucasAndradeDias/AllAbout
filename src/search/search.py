from flask import Blueprint, jsonify, request


#local modules
from .services.request_service import verify_query_string
from .services import searchservices



search_bp = Blueprint('search',__name__,url_prefix="/search")


handle_request = searchservices.service_web_scraping()


@search_bp.route("/")
@verify_query_string
def term():

    term = request.args.get("term")

    wc = handle_request.control_scraping(term)

    response_json = jsonify(wc)

    return response_json,200
