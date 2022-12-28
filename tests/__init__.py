import json
from src import create_app

import pytest

app = create_app().test_client()



def search_simple_term_without_arg():
    response = app.get('/search')

    assert response.status_code == 200



def search_term_forum():  

    data = {"term":"examples"}

    response = app.get('/search/forums',query_string=data)

    assert response.status_code == 200

    res = json.loads(response.data.decode('utf-8'))

    assert "reddit" in res
    assert res["reddit"] != []    


def search_term_news():

    data = {'term':"brasil"}
    response = app.get("/search/news",query_string=data)

    assert response.status_code == 200

    res =json.loads(response.data.decode("utf-8"))

    assert "news" in res 
    assert res["news"] != []

    
search_term_news()
search_term_forum()