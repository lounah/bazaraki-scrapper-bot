import threading

from bot.controller import BotController
from logger.logger import Logger


class Bot:
    def __init__(self, controller: BotController, logger: Logger):
        self._controller = controller
        self._logger = logger

    def start(self):
        try:
            self._logger.debug(f"[Bot] bot started")
            self._controller.start()
        except Exception as e:
            self._logger.error(f"[Bot] {str(e)}")
