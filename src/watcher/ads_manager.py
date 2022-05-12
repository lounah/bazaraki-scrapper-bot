from typing import List

from src.api.bazaraki_api import BazarakiApi
from src.api.district import District
from src.db.ads import AdsDatabase
from src.scrapper.ad import Ad, Category
from src.scrapper.scrapper import Scrapper

MIN_PRICE = 0
MAX_RENT_PRICE = 3200
MAX_CAR_PRICE = 35000
STUB_CARS_QUERY = ""


class AdsManager:
    def __init__(self, api: BazarakiApi, scrapper: Scrapper, db: AdsDatabase):
        self._api = api
        self._db = db
        self._scrapper = scrapper

    def request_updates(self) -> List[Ad]:
        remote = self._get_ads()
        local = self._db.all()
        updates = list(filter(lambda ad: ad not in local, remote))
        self._db.add_all(updates)
        return updates

    def _get_ads(self) -> List[Ad]:
        estate_html = self._api.get_estate(District.values(), MIN_PRICE, MAX_RENT_PRICE)
        cars_html = self._api.get_cars(District.values(), MIN_PRICE, MAX_CAR_PRICE, STUB_CARS_QUERY)
        estate = self._scrapper.scrap(estate_html, Category.ESTATE)
        cars = self._scrapper.scrap(cars_html, Category.CARS)
        return estate + cars
