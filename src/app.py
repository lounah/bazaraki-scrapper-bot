import os

from di.di import Di


def main():
    di = Di(os.getenv('token'), os.getenv('port'), os.getenv('url'), os.getenv('cert'), os.getenv('key'))
    di.bot().start()


if __name__ == "__main__":
    main()
