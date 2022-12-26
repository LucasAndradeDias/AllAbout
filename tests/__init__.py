import json
from src import create_app

import pytest

app = create_app().test_client()



def search_simple_term():

    response = app.get('/search/term')

    res = json.loads(response.data.decode('utf-8')).get("links")

    print(type(res))

    assert not "title" in res[0]

    assert response.status_code == 200
    



search_simple_term()