from typing import List

from core.data.district import District
from core.data.estate import Estate
from core.data.estate_db import EstateDatabase
from core.domain.get_estate import GetEstate


class EstateRepository:
    def __init__(self, get_estate: GetEstate, database: EstateDatabase):
        self._get_estate = get_estate
        self._db = database

    def get_updates(self, districts: List[District], price_min: int, price_max: int) -> List[Estate]:
        estates = self._get_estate.execute(districts, price_min, price_max)
        saved = self._db.get_all()
        updates = list(filter(lambda estate: estate not in saved, estates))
        self._db.add_all(updates)
        return updates
