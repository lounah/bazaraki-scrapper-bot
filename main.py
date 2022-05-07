import logging

from di import Di
import daemon

TOKEN = "5168767958:AAEk_XoqEaS9S8bxy9qfBeFiAIg5Xi20okE"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    with daemon.DaemonContext():
        Di(TOKEN, 30).get_bot().start()


if __name__ == "__main__":
    main()
