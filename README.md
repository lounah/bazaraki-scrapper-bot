# Bazaraki Scrapper Bot

A simple Telegram bot, which automates search routine in Cyprus
by polling www.bazaraki.com for new ads every 5 minutes.

---

## Features

- Cars advertisements in Cyprus;
- Properties to rent advertisements in Cyprus;

## Usage

[Telegram](https://t.me/bazaraki_watcher_bot)

## Deployment

### Build docker image

```shell
$ docker build -t bazaraki-scrapper-bot .
```

### Create .env file

```shell
token=<Telegram Bot Token> # obtain it from @botfather
port=<PORT> # opened port on your machine for webhook
url=<URL> # public url of host machine (e.g. https://37.139.43.8
cert=<CERT_PATH> # path to .pem file with certificates
key=<KEY_PATH> # path to .key secret
```

### Run

```shell
$ docker run --rm -d --env-file your-env-file.env bazaraki-scrapper-bot
```
