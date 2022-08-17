from typing import Any, Dict, Tuple
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


def main(query: str, model_params: Dict[str, Any], page: int, batch: int = 5) -> Tuple[Dict[str, Any], str]:
    """
    Main function to run the entire pipeline.
    """

    # Get the search results
    # Returns a dictionary with the article title as a key and the time
    # it took to return the search
    search_results, search_time = custom_search(query, page)

    # Added batching to lessen the # of iterations for
    # large queries

    i = 0
    # Done like this to make it easy to remove later
    for result in search_results:
        if i < batch:
            (search_results[result]["web_text"]) = get_website_text(
                search_results[result]["url"]
            )

    # Create the summary for each article
    for result in search_results:
        if "web_text" in search_results[result]:
            search_results[result]["tldr"] = create_summary(
                search_results[result]["web_text"],
                model_params["model"],
                model_params["max_tokens"],
                model_params["n_generations"],
                model_params["temperature"],
                model_params["k"],
                model_params["p"],
            )
            search_results[result]['web_text'] = ''
    
    return search_results, search_time


if __name__ == "__main__":
    print(main("Braised Short Ribs", test_model_params, 1)['Braised Short Ribs Recipe - Tastes Better From Scratch'])
