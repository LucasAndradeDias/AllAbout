import json
from src import create_app

import pytest

app = create_app().test_client()



def search_simple_term_without_arg():
    response = app.get('/search')

    assert response.status_code == 200



def search_simple_term_with_arg():  

    data = {"term":"examples"}

    response = app.get('/search',query_string=data)

    #res = json.loads(response.data.decode('utf-8'))


    assert response.status_code == 200
    #assert "reddit_posts" in res
    # assert res["reddit_posts"] != []

    


#search_simple_term_without_arg()
search_simple_term_with_arg()