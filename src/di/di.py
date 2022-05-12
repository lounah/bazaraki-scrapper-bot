import os

from api.bazaraki_api import BazarakiApi
from bot.bot import Bot
from bot.config import ServerConfig
from bot.controller import BotController
from db.ads import AdsDatabase
from db.subscriptions import SubscriptionsDatabase
from logger.logger import LoggerImpl, SystemOutTarget, FileTarget
from scrapper.scrapper import Scrapper
from watcher.ads_manager import AdsManager
from watcher.ads_watcher import AdsWatcher

POLLING_TIMEOUT = 60 * 5
LOGS_PATH = 'outputs/logs.txt'
ADS_PATH = 'outputs/ads.json'
SUBSCRIPTIONS_PATH = 'outputs/subscriptions.json'


class Di:
    def __init__(self, token: str, port: str, url: str, cert: str, key: str):
        self._config = ServerConfig(token, int(port), url, cert, key)
        self._init_outputs()

    def bot(self) -> Bot:
        logger = LoggerImpl([SystemOutTarget(), FileTarget(LOGS_PATH)])
        ads_db = AdsDatabase(ADS_PATH)
        subs_db = SubscriptionsDatabase(SUBSCRIPTIONS_PATH)
        manager = AdsManager(BazarakiApi(), Scrapper(), ads_db, subs_db)
        watcher = AdsWatcher(POLLING_TIMEOUT, manager, logger)
        controller = BotController(self._config, watcher, subs_db, logger)
        return Bot(controller, logger)

    @staticmethod
    def _init_outputs():
        os.makedirs(os.path.dirname(ADS_PATH), exist_ok=True)
        os.makedirs(os.path.dirname(SUBSCRIPTIONS_PATH), exist_ok=True)
