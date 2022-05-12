import os
import sys

from di.di import Di


def main(argv):
    di = Di(os.getenv('token'), os.getenv('port'), os.getenv('url'), os.getenv('cert'), os.getenv('key'))
    di.bot().start()


if __name__ == "__main__":
    main(sys.argv)
