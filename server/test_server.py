from multiprocessing.spawn import import_main_path


import requests
import sys
import os

TEST_URL = "http://127.0.0.1:8080"
PRODUCTION_URL = "https://tldr-production.up.railway.app"


def test_search():
    resp = requests.get(TEST_URL)
    response = requests.post(TEST_URL + "/search/Sustainability/{0}".format(1))
    print(resp.json(), "\n", response.json())

def test_main():
    sys.path.append("C:/Users/Michael/OneDrive/Documents/GitHub/tldr/")

    from data import main

    

test_search()
