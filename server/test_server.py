from multiprocessing.spawn import import_main_path


import requests

TEST_URL = 'http://127.0.0.1:8080'

def test_search():
    response = requests.post(TEST_URL + '/search/Python/{0}'.format(1))
    print(response.json())

test_search()