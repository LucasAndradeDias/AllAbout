from flask import Blueprint, jsonify, request

#local modules
from .services.request_service import verify_query_string
from .services import searchservices



search_bp = Blueprint('search',__name__,url_prefix="/search")



@search_bp.route("/")
@verify_query_string
def all_data():
    """
    RETURNS ALL DATAS FROM NEWS AND FORUNS
    """

    term = request.args.get("term")

    return 200




# GET ONLY POSTS IN FORUMS 
@search_bp.route("/forums")
@verify_query_string
def get_only_foruns_data():
    
    term_to_search = request.args.get("term")

    data = searchservices.service_control().get_all_forums_data_term(term=term_to_search)

    response_json = jsonify(data)

    return response_json,200



## GET ONLY NEWS 

@search_bp.route("/news")
@verify_query_string
def get_news_term():

    #term to search
    term = request.args.get("term")

    #getting news
    news_array = searchservices.service_control().get_news_from_site_term(term)

    response_dict = {"news":news_array} 

    #convert into json to response
    response_json = jsonify(response_dict)

    #response 
    return response_json,200


## get all data
@search_bp.route("/all")
@verify_query_string
def get_all_data():
    term = request.args.get("term")

    service = searchservices.service_control()

    news = service.get_news_from_site_term(term=term)

    forums = service.get_all_forums_data_term(term=term)

    response_dict = {"news":news,"forums":forums}

    response_json = jsonify(response_dict)

    return response_json,200
    







