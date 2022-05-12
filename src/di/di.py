import os

from src.api.bazaraki_api import BazarakiApi
from src.bot.bot import Bot
from src.bot.config import ServerConfig
from src.bot.controller import BotController
from src.db.ads import AdsDatabase
from src.db.subscriptions import SubscriptionsDatabase
from src.logger.logger import LoggerImpl, SystemOutTarget, FileTarget
from src.scrapper.scrapper import Scrapper
from src.watcher.ads_manager import AdsManager
from src.watcher.ads_watcher import AdsWatcher

POLLING_TIMEOUT = 60 * 5
LOGS_PATH = '../outputs/logs.txt'
ADS_PATH = '../outputs/ads.json'
SUBSCRIPTIONS_PATH = '../outputs/subscriptions.json'


class Di:
    def __init__(self, token: str, port: str, url: str, cert: str, key: str):
        self._config = ServerConfig(token, int(port), url, cert, key)
        self._init_outputs()

    def bot(self) -> Bot:
        logger = LoggerImpl([SystemOutTarget(), FileTarget(LOGS_PATH)])
        manager = AdsManager(BazarakiApi(), Scrapper(), AdsDatabase(ADS_PATH))
        watcher = AdsWatcher(POLLING_TIMEOUT, manager, logger)
        controller = BotController(self._config, watcher, SubscriptionsDatabase(SUBSCRIPTIONS_PATH), logger)
        return Bot(controller, logger)

    @staticmethod
    def _init_outputs():
        os.makedirs(os.path.dirname(ADS_PATH), exist_ok=True)
        os.makedirs(os.path.dirname(SUBSCRIPTIONS_PATH), exist_ok=True)
