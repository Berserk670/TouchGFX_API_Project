from clients.rapid_api import rapid_api_web_search


def get_images(search_term):
    image_search_results = rapid_api_web_search.get_images_by_search_term(
        search_term, 2
    )
    return image_search_results
