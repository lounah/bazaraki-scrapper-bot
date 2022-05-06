from di import Di

TOKEN = "5168767958:AAEk_XoqEaS9S8bxy9qfBeFiAIg5Xi20okE"


def main():
    Di(TOKEN, 30).get_bot().start()


if __name__ == "__main__":
    main()
