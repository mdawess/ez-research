
import requests
import os

API_KEY = os.environ.get('GOOGLE_API_KEY')
SEARCH_ENGINE_ID = os.environ.get('cw')

TEST_QUERY = 'python'

page = 1  # As a test
start = (page - 1) * 10 + 1

url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={TEST_QUERY}&start={start}"

data = requests.get(url).json()

print(data)
