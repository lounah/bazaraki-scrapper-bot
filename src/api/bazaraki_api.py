from typing import List

import requests

from api.district import District


class BazarakiApi:
    def __init__(self):
        self.url = "https://www.bazaraki.com"

    def get_estate(self, districts: List[District], price_min: int, price_max: int) -> str:
        _url = f"{self.url}/real-estate/houses-and-villas-rent"
        _params = {"cities": districts, "price_min": price_min, "price_max": price_max}
        return requests.post(url=_url, params=_params).text

    def get_cars(self, districts: List[District], price_min: int, price_max: int, q: str) -> str:
        _url = f"{self.url}/car-motorbikes-boats-and-parts/cars-trucks-and-vans"
        _params = {"cities": districts, "price_min": price_min, "price_max": price_max, "q": q}
        return requests.post(url=_url, params=_params).text
