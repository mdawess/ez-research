from typing import Dict
from query import custom_search
from web_scraper import get_website_text
from summarize import create_summary

main_model_params = {
    'model': 'small',
    'max_tokens': 100,
    'n_generations': 5,
    'temperature': 0.7,
    'k': 0,
    'p': 0.75,
}

def main(query: str, model_params: Dict[str], page: int) -> Dict[Dict[str]]:
    """
    Main function to run the entire pipeline.
    """
    
    # Get the search results
    # Returns a dictionary with the article title as a key and the time
    # it took to return the search
    search_results, search_time = custom_search(query, page)

    for result in search_results:
        pass
