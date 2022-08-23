from multiprocessing.spawn import import_main_path


import requests

TEST_URL = 'http://0.0.0.0:8080/'

def test_search():
    response = requests.get(TEST_URL + '/search/Python/1}')
    # assert response.json()['status'] == 'healthy'
    print(response.json())