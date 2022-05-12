import re
from typing import List

from telegram import ParseMode, ForceReply
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

from src.bot.config import ServerConfig
from src.bot.messages import keyboards, messages
from src.bot.subscriptions import Subscription
from src.db.subscriptions import SubscriptionsDatabase
from src.logger.logger import Logger
from src.scrapper.ad import Ad
from src.watcher.ads_watcher import AdsWatcher


class BotController:
    def __init__(self,
                 config: ServerConfig,
                 watcher: AdsWatcher,
                 subs_db: SubscriptionsDatabase,
                 logger: Logger):
        self._config = config
        self._updater = Updater(config.token)
        self._watcher = watcher
        self._subs_db = subs_db
        self._logger = logger

    def start(self):
        self._start_watcher()
        self._start_bot()

    def _start_watcher(self):
        self._watcher.start(callback=self._handle_new_ads)

    def _start_bot(self):
        self._init_dispatcher()
        self._updater.start_webhook(
            listen='0.0.0.0',
            port=self._config.port,
            cert=self._config.cert,
            key=self._config.key,
            url_path=self._config.token,
            webhook_url=self._config.hook_url()
        )
        self._updater.idle()

    def _init_dispatcher(self):
        self._updater.dispatcher.add_handler(CommandHandler(['start'], self._cmd_start))
        self._updater.dispatcher.add_handler(CommandHandler(['subscription'], self._cmd_subscription))
        self._updater.dispatcher.add_handler(CommandHandler(['support'], self._cmd_support))
        self._updater.dispatcher.add_handler(CommandHandler(['unsubscribe'], self._cmd_unsubscribe))
        self._updater.dispatcher.add_handler(CallbackQueryHandler(self._cmd_search_houses, pattern='houses_search'))
        self._updater.dispatcher.add_handler(
            CallbackQueryHandler(self._cmd_district_houses_back, pattern='houses_district_back'))
        self._updater.dispatcher.add_handler(CallbackQueryHandler(self._cmd_search_cars, pattern='cars_search'))
        self._updater.dispatcher.add_handler(
            CallbackQueryHandler(self._cmd_district_cars_back, pattern='cars_district_back'))
        self._updater.dispatcher.add_handler(
            CallbackQueryHandler(self._cmd_district_houses, pattern='^houses_district.*'))
        self._updater.dispatcher.add_handler(CallbackQueryHandler(self._cmd_district_cars, pattern='^cars_district.*'))
        self._updater.dispatcher.add_handler(
            CallbackQueryHandler(self._cmd_price_min_houses, pattern='^houses_price_min.*'))
        self._updater.dispatcher.add_handler(
            CallbackQueryHandler(self._cmd_price_min_houses_back, pattern='houses_price_min_back'))
        self._updater.dispatcher.add_handler(
            CallbackQueryHandler(self._cmd_price_min_cars_back, pattern='cars_price_min_back'))
        self._updater.dispatcher.add_handler(
            CallbackQueryHandler(self._cmd_price_min_cars, pattern='^cars_price_min.*'))
        self._updater.dispatcher.add_handler(
            CallbackQueryHandler(self._cmd_price_max_houses_back, pattern='houses_price_max_back'))
        self._updater.dispatcher.add_handler(
            CallbackQueryHandler(self._cmd_price_max_houses, pattern='^houses_price_max.*'))
        self._updater.dispatcher.add_handler(
            CallbackQueryHandler(self._cmd_price_max_cars_back, pattern='cars_price_max_back'))
        self._updater.dispatcher.add_handler(
            CallbackQueryHandler(self._cmd_price_max_cars, pattern='^cars_price_max.*'))
        self._updater.dispatcher.add_handler(MessageHandler(Filters.reply, self._cmd_query_cars))

    def _cmd_start(self, update, ctx):
        self._logger.info(f"new subscription `{update.message.chat_id}`")
        self._subs_db.add(Subscription.new(str(update.message.chat_id)))
        update.message.reply_text(messages['start'], reply_markup=keyboards['start'])

    def _cmd_subscription(self, update, ctx):
        subscription = self._subs_db.get(str(update.message.chat_id))
        update.message.reply_text(str(subscription), parse_mode=ParseMode.HTML)

    def _cmd_unsubscribe(self, update, ctx):
        self._logger.info(f"unregister subscription `{update.message.chat_id}`")
        self._subs_db.remove(str(update.message.chat_id))
        update.message.reply_text(messages['unsubscribe'])

    def _cmd_support(self, update, ctx):
        self._logger.debug(f"ask for support `{update.message.chat_id}`")
        update.message.reply_text(messages['support'])

    def _cmd_search_houses(self, update, ctx):
        self._logger.debug(f"search houses for `{update.callback_query.message.chat_id}`")
        update.callback_query.edit_message_text(
            messages['district'],
            parse_mode=ParseMode.HTML,
            reply_markup=keyboards['houses_districts']
        )

    @staticmethod
    def _cmd_district_houses_back(update, ctx):
        update.callback_query.edit_message_text(
            messages['start'],
            parse_mode=ParseMode.HTML,
            reply_markup=keyboards['start']
        )

    def _cmd_search_cars(self, update, ctx):
        self._logger.debug(f"search cars for `{update.callback_query.message.chat_id}`")
        update.callback_query.edit_message_text(
            messages['district'],
            parse_mode=ParseMode.HTML,
            reply_markup=keyboards['cars_districts']
        )

    @staticmethod
    def _cmd_district_cars_back(update, ctx):
        update.callback_query.edit_message_text(
            messages['start'],
            parse_mode=ParseMode.HTML,
            reply_markup=keyboards['start']
        )

    def _cmd_district_houses(self, update, ctx):
        chat_id = update.callback_query.message.chat_id
        district = re.search("\d+", update.callback_query.data).group(0)
        self._subs_db.update(str(chat_id), ['estate', 'district'], district)
        update.callback_query.edit_message_text(
            messages['price_min'],
            parse_mode=ParseMode.HTML,
            reply_markup=keyboards['houses_price_min']
        )

    def _cmd_district_cars(self, update, ctx):
        chat_id = update.callback_query.message.chat_id
        district = re.search("\d+", update.callback_query.data).group(0)
        self._subs_db.update(str(chat_id), ['car', 'district'], district)
        update.callback_query.edit_message_text(
            messages['price_min'],
            parse_mode=ParseMode.HTML,
            reply_markup=keyboards['cars_price_min']
        )

    def _cmd_price_min_houses(self, update, ctx):
        chat_id = update.callback_query.message.chat_id
        min_price = re.search("\d+", update.callback_query.data).group(0)
        self._subs_db.update(str(chat_id), ['estate', 'price_min'], min_price)
        update.callback_query.edit_message_text(
            messages['price_max'],
            parse_mode=ParseMode.HTML,
            reply_markup=keyboards['houses_price_max']
        )

    @staticmethod
    def _cmd_price_min_houses_back(update, ctx):
        update.callback_query.edit_message_text(
            messages['district'],
            parse_mode=ParseMode.HTML,
            reply_markup=keyboards['houses_districts']
        )

    def _cmd_price_min_cars(self, update, ctx):
        chat_id = str(update.callback_query.message.chat_id)
        min_price = re.search("\d+", update.callback_query.data).group(0)
        self._subs_db.update(chat_id, ['car', 'price_min'], min_price)
        update.callback_query.edit_message_text(
            messages['price_max'],
            parse_mode=ParseMode.HTML,
            reply_markup=keyboards['cars_price_max']
        )

    @staticmethod
    def _cmd_price_min_cars_back(update, ctx):
        update.callback_query.edit_message_text(
            messages['district'],
            parse_mode=ParseMode.HTML,
            reply_markup=keyboards['cars_districts']
        )

    def _cmd_price_max_houses(self, update, ctx):
        chat_id = str(update.callback_query.message.chat_id)
        max_price = re.search("\d+", update.callback_query.data).group(0)
        self._subs_db.update(chat_id, ['estate', 'price_max'], max_price)
        update.callback_query.edit_message_text(messages['configured'], parse_mode=ParseMode.HTML)

    @staticmethod
    def _cmd_price_max_houses_back(update, ctx):
        update.callback_query.edit_message_text(
            messages['price_min'],
            parse_mode=ParseMode.HTML,
            reply_markup=keyboards['houses_price_min']
        )

    def _cmd_price_max_cars(self, update, ctx):
        chat_id = str(update.callback_query.message.chat_id)
        max_price = re.search("\d+", update.callback_query.data).group(0)
        self._subs_db.update(chat_id, ['car', 'price_max'], max_price)
        update.callback_query.message.reply_text(
            messages['car_query'],
            parse_mode=ParseMode.HTML,
            reply_markup=ForceReply(selective=True)
        )

    def _cmd_query_cars(self, update, ctx):
        self._subs_db.update(str(update.message.chat_id), ['car', 'query'], update.message.text)
        update.message.reply_text(messages['configured'], parse_mode=ParseMode.HTML)

    @staticmethod
    def _cmd_price_max_cars_back(update, ctx):
        update.callback_query.edit_message_text(
            messages['price_min'],
            parse_mode=ParseMode.HTML,
            reply_markup=keyboards['cars_price_min']
        )

    def _handle_new_ads(self, ads: List[Ad]):
        for subscription in self._subs_db.all():
            for ad in ads:
                if ad.matches_subscription(subscription):
                    self._updater.bot.send_message(
                        chat_id=subscription.id,
                        parse_mode=ParseMode.HTML,
                        text=str(ad)
                    )
