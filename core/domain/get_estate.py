from typing import List

from core.data.bazaraki_api import BazarakiApi
from core.data.district import District
from core.data.estate import Estate
from core.domain.estate_mapper import EstateMapper


class GetEstate:
    def __init__(self, api: BazarakiApi, mapper: EstateMapper):
        self._api = api
        self._mapper = mapper

    def execute(self, districts: List[District], price_min: int, price_max: int) -> List[Estate]:
        _response_html = self._api.get_rentals(districts, price_min, price_max)
        return self._mapper.map(_response_html)
