from bot.bazaraki_bot import BazarakiBot
from core.data.bazaraki_api import BazarakiApi
from core.data.estate_db import EstateDatabase
from core.data.subscription_manager import SubscriptionManager
from core.domain.estate_mapper import EstateMapper
from core.domain.estate_repository import EstateRepository
from core.domain.get_estate import GetEstate
from core.logger.logger import Logger


class Di:
    def __init__(self, token: str, poll_timeout: int):
        self._token = token
        self._timeout = poll_timeout

    def get_bot(self):
        get_estate = GetEstate(BazarakiApi(), EstateMapper())
        db = EstateDatabase("estates.json")
        repository = EstateRepository(get_estate, db)
        subscription_manager = SubscriptionManager("subscriptions.json")
        logger = Logger("logs.txt")
        return BazarakiBot(self._token, self._timeout, repository, subscription_manager, logger)
