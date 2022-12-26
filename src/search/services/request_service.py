from functools import wraps

from flask import request,make_response

def verify_query_string(req):
    """
        Verify if the request has at least one query string
    """
    @wraps(req)
    def query_string(*args, **kwargs):
        if request.args: 
            return req(*args, **kwargs)
        else:
            return make_response ({"message":"the request does not have an valid argument"},400)

    return query_string


