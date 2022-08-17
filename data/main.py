from typing import Any, Dict
from query import custom_search
from web_scraper import get_website_text
from summarize import create_summary

test_model_params = {
    "model": "small",
    # Tokens are the number of characters returned in the summary
    "max_tokens": 300,
    "n_generations": 5,
    "temperature": 0.7,
    "k": 0,
    "p": 0.75,
}

production_model_params = {
    "model": "main",
    # Tokens are the number of characters returned in the summary
    "max_tokens": 300,
    "n_generations": 7,
    "temperature": 0.7,
    "k": 0,
    "p": 0.75,
}


def main(query: str, model_params: Dict[str, Any], page: int) -> Any:
    """
    Main function to run the entire pipeline.
    """

    # Get the search results
    # Returns a dictionary with the article title as a key and the time
    # it took to return the search
    search_results, search_time = custom_search(query, page)

    for result in search_results:
        (search_results[result]["web_text"]) = get_website_text(
            search_results[result]["url"]
        )

    return search_results


if __name__ == "__main__":
    print(main("Braised Short Ribs", test_model_params, 1))
