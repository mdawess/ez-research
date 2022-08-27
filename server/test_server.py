from multiprocessing.spawn import import_main_path


import requests

TEST_URL = "http://127.0.0.1:8080"
PRODUCTION_URL = "https://tldr-production.up.railway.app"


def test_search():
    resp = requests.get(PRODUCTION_URL)
    response = requests.post(PRODUCTION_URL + "/search/Python/{0}".format(1))
    print(resp.json(), "\n", response.json())


test_search()
