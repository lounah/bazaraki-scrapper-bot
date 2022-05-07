import logging

from di import Di
from daemonize import Daemonize

TOKEN = "5168767958:AAEk_XoqEaS9S8bxy9qfBeFiAIg5Xi20okE"

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    Di(TOKEN, 30).get_bot().start()


if __name__ == "__main__":
    daemon = Daemonize(app="test_app", pid='666', action=main)
    daemon.start()
