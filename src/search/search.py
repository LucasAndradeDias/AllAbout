from flask import Blueprint, jsonify, request

#local modules
from .services.request_service import verify_query_string

from .services import service_control


# Blueprint config
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

    data = service_control().search_forum_term(term=term_to_search)

    response_json = jsonify(data)

    return response_json,200



## GET ONLY NEWS 

@search_bp.route("/news")
@verify_query_string
def get_news_term():

    #term to search
    term = request.args.get("term")

    #getting news
    news_array = service_control().search_news_term(term)

    #convert into json to response
    response_json = jsonify(news_array)

    #response 
    return response_json,200


## get all data
@search_bp.route("/all")
@verify_query_string
def get_all_data():

    #term to make the search
    term = request.args.get("term")

    service = service_control()
    try:

        datas_found = [service.search_news_term(term=term),service.search_forum_term(term=term)]

        
        response_dict = {"found":datas_found}

        response_json = jsonify(response_dict)

        return response_json,200

    except TypeError as err:
        
        print(err)

        response_json = jsonify({"msg":"There were an error with your request"})

        return response_json,500
        







