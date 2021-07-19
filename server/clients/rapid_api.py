import requests
from dotenv import dotenv_values

config = dotenv_values(".env")


class RapidAPI:
    def __init__(self):
        self.api_url = config["API_HOST"]
        self.api_key = config["API_KEY"]
        self.headers = {"x-rapidapi-key": self.api_key, "x-rapidapi-host": self.api_url}
        self.image_search_url = config["IMAGE_SEARCH_URL"]

    def get_images_by_search_term(self, search_term, page_number=None, page_size=None):
        query_string = {
            "q": search_term,
            "pageNumber": page_number if page_number else 1,
            "pageSize": page_size if page_size else 10,
            "autoCorrect": False,
        }

        try:
            response = requests.request(
                "GET", self.image_search_url, headers=self.headers, params=query_string
            )

            return response.json()

        except Exception as e:
            return {"error": str(e)}


rapid_api_web_search = RapidAPI()
