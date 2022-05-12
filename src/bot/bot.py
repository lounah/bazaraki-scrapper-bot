import threading

from src.bot.controller import BotController
from src.logger.logger import Logger


class Bot:
    def __init__(self, controller: BotController, logger: Logger):
        self._controller = controller
        self._logger = logger

    def start(self):
        try:
            self._logger.debug(f"[Bot] bot started")
            threading.Thread(target=self._controller.start).start()
        except Exception as e:
            self._logger.error(f"[Bot] {str(e)}")
