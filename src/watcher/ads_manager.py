from typing import List

from src.api.bazaraki_api import BazarakiApi
from src.api.district import District
from src.db.ads import AdsDatabase
from src.db.subscriptions import SubscriptionsDatabase
from src.scrapper.ad import Ad, Category
from src.scrapper.scrapper import Scrapper

MIN_PRICE = 0
MAX_RENT_PRICE = 3200


class AdsManager:
    def __init__(self, api: BazarakiApi, scrapper: Scrapper, ads_db: AdsDatabase, subs_db: SubscriptionsDatabase):
        self._api = api
        self._ads_db = ads_db
        self._subs_db = subs_db
        self._scrapper = scrapper

    def request_updates(self) -> List[Ad]:
        remote = self._get_estate_ads() + self._get_cars_ads()
        local = self._ads_db.all()
        updates = list(filter(lambda ad: ad not in local, remote))
        self._ads_db.add_all(updates)
        return updates

    def _get_estate_ads(self) -> List[Ad]:
        estate_html = self._api.get_estate(District.values(), MIN_PRICE, MAX_RENT_PRICE)
        return self._scrapper.scrap(estate_html, Category.ESTATE)

    def _get_cars_ads(self) -> List[Ad]:
        result = []
        for subscription in self._subs_db.all():
            district = District(subscription.car.district)
            min_price = subscription.car.price_min
            max_price = subscription.car.price_max
            query = subscription.car.query
            cars_html = self._api.get_cars([district], min_price, max_price, query)
            result.extend(self._scrapper.scrap(cars_html, Category.CARS))
        return result
