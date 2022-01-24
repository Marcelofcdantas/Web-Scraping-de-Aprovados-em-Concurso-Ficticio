import requests
from time import sleep
from parsel import Selector


class Scraping:

    def fetch(delay = 1, timeout = 3):
        url = 'https://sample-university-site.herokuapp.com'
        try:
            sleep(delay)
            response = requests.get(url, timeout=timeout)
        except (requests.ReadTimeout, requests.HTTPError):
            return None
        else:
            if response.status_code == 200:
                return response.text



print(Scraping.fetch())