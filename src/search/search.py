from flask import Blueprint, jsonify

from .services import searchservices

search_bp = Blueprint('search',__name__,url_prefix="/search")


handle_request = searchservices.service_web_scraping()


@search_bp.route("/term")
def term():

    wc = handle_request.download_page("brasil")

    print(wc)

    return "hello world"
