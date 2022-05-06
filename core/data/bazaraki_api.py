from typing import List

import requests as requests
from aiohttp import ClientSession

from core.data.district import District


class BazarakiApi:
    def __init__(self):
        self.url = "https://www.bazaraki.com"
        self._session = ClientSession()

    def get_rentals(self, districts: List[District], price_min: int, price_max: int) -> str:
        _url = f"{self.url}/real-estate/houses-and-villas-rent"
        _params = {"cities": districts, "price_min": price_min, "price_max": price_max}
        return requests.post(url=_url, params=_params).text
