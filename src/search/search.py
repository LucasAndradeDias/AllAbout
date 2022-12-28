from flask import Blueprint, jsonify, request

#local modules
from .services.request_service import verify_query_string
from .services import searchservices



search_bp = Blueprint('search',__name__,url_prefix="/search")



@search_bp.route("/")
@verify_query_string
def term():
    """
    RETURNS ALL DATAS FROM NEWS AND FORUNS
    """

    term = request.args.get("term")

    wc = handle_request.control_scraping(term)

    response_json = jsonify(wc)

    return response_json,200





@search_bp.route("/forums")
@verify_query_string
def get_only_foruns_data():
    
    term_to_search = request.args.get("term")

    data = searchservices.service_for_forums().get_all_forums_data(term=term_to_search)

    response_json = jsonify(data)

    return response_json,200













