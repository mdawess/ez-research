# External Imports
from typing import Any, Dict, Tuple
import os.path
import sys
import cohere

# Internal Imports
sys.path.append("C:/Users/Michael/OneDrive/Documents/GitHub/tldr/data")
import Search
import Scraper
import Summarizer

API_KEY = os.environ.get("GOOGLE_API_KEY")
CO = cohere.Client(os.environ.get("COHERE_API_KEY"))
CX = os.environ.get("CX")
URL = "https://www.googleapis.com/customsearch/v1"

test_model_params = {
    "model": "small",
    "max_tokens": 300,
    "n_generations": 5,
    "temperature": 0.7,
    "k": 0,
    "p": 0.75,
}

production_model_params = {
    "model": "large",
    "max_tokens": 300,
    "n_generations": 7,
    "temperature": 0.7,
    "k": 0,
    "p": 0.75,
}

class TLDR:

    def __init__(self):
        self.query = Search(API_KEY, CX, URL)
        self.web_scraper = Scraper()
        self.summarizer = Summarizer()
        self.model_params = {}

    def init_params(self, model: str) -> None:
        """
        Initialize the model parameters for the summarizer.
        """
        if model == "test":
            self.model_params = test_model_params
        elif model == "production":
            self.model_params = production_model_params
        else:
            raise ValueError("Invalid model parameter")

    def tldr(
        self,
        query: str,
        batch: int = 5,
        ) -> Tuple[Dict[str, Any], str]:
        """
        Main function to run the entire pipeline and return the tldr.
        """

        # Get the search results
        # Returns a dictionary with the article title as a key and the time
        # it took to return the search
        search_results, search_time = self.query.custom_search(query)

        # Added batching to lessen the # of iterations for
        # large queries

        i = 0
        # Done like this to make it easy to remove later
        for result in search_results:
            if i < batch:
                search_results[result]["web_text"] = self.web_scraper.get_website_text(
                    search_results[result]["url"]
                )

        # Create the summary for each article
        for result in search_results:
            if "web_text" in search_results[result]:
                search_results[result]["tldr"] = self.summarizer.create_summary(
                    search_results[result]["web_text"],
                    self.model_params["model"],
                    self.model_params["max_tokens"],
                    self.model_params["n_generations"],
                    self.model_params["temperature"],
                    self.model_params["k"],
                    self.model_params["p"],
                )
                search_results[result]["web_text"] = ""

        return search_results, search_time


if __name__ == "__main__":
    tldr = TLDR()
    tldr.init_params("test")
    print(tldr.tldr("Braised Short Ribs", 1))
