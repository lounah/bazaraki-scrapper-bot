import threading
import time

from logger.logger import Logger
from watcher.ads_manager import AdsManager


class AdsWatcher:
    def __init__(self, timeout: int, ads_manager: AdsManager, logger: Logger):
        self._timeout = timeout
        self._manager = ads_manager
        self._logger = logger

    def start(self, callback):
        try:
            threading.Thread(target=self._watch, args=([lambda ads: callback(ads)])).start()
        except Exception as e:
            self._logger.error(f"[AdsWatcher] {str(e)}")

    def _watch(self, callback):
        while True:
            self._logger.debug("[AdsWatcher] polling www.bazaraki.com")
            new_ads = self._manager.request_updates()
            self._logger.debug(f"[AdsWatcher] found {len(new_ads)} new ads")
            callback(new_ads)
            time.sleep(self._timeout)
