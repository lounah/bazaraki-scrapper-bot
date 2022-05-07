import re
import threading
import time
from datetime import datetime
from typing import List

from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

from bot import messages
from core.data.district import District
from core.data.estate import Estate
from core.domain.estate_repository import EstateRepository
from core.data.subscription_manager import SubscriptionManager


class BazarakiBot:
    def __init__(self,
                 token: str,
                 timeout_sec: int,
                 estate_repo: EstateRepository,
                 subscription_manager: SubscriptionManager):
        self._token = token
        self._updater = Updater(token)
        self._timeout = timeout_sec
        self._repo = estate_repo
        self._subscription_manager = subscription_manager

    def start(self):
        threading.Thread(target=self._configure_bot).start()
        threading.Thread(target=self._poll_bazaraki).start()

    def _configure_bot(self):
        self._updater.dispatcher.add_handler(CommandHandler(['start', 'configure'], self._start_cmd))
        self._updater.dispatcher.add_handler(CallbackQueryHandler(self._district_cmd, pattern='^district$'))
        self._updater.dispatcher.add_handler(CallbackQueryHandler(self._district_selected, pattern='^district.*'))
        self._updater.dispatcher.add_handler(CallbackQueryHandler(self._min_price_selected, pattern='^price_min.*'))
        self._updater.dispatcher.add_handler(CallbackQueryHandler(self._max_price_selected, pattern='^price_max.*'))
        self._updater.dispatcher.add_handler(CallbackQueryHandler(self._district_back, pattern='^back_district$'))
        self._updater.dispatcher.add_handler(CallbackQueryHandler(self._min_price_back, pattern='^back_price_min$'))
        self._updater.dispatcher.add_handler(CallbackQueryHandler(self._max_price_back, pattern='^back_price_max$'))
        self._updater.start_webhook(listen='0.0.0.0',
                                    port=8443,
                                    cert='cert.pem',
                                    key='private.key',
                                    url_path=self._token,
                                    webhook_url=f'https://37.139.43.8:8443/{self._token}')
        self._updater.idle()

    def _start_cmd(self, update, context):
        chat_id = update.message.chat_id
        self._subscription_manager.register(str(chat_id))
        update.message.reply_text(
            messages.messages['start'],
            reply_markup=messages.keyboards['configure']
        )

    @staticmethod
    def _district_cmd(update, context):
        update.callback_query.edit_message_text(
            messages.messages['district'],
            reply_markup=messages.keyboards['district']
        )

    def _district_selected(self, update, context):
        chat_id = update.callback_query.message.chat_id
        district = re.search("\d+", update.callback_query.data).group(0)
        self._subscription_manager.update(chat_id, {"districts": [int(district)]})
        update.callback_query.edit_message_text(
            messages.messages['price_min'],
            parse_mode=ParseMode.MARKDOWN_V2,
            reply_markup=messages.keyboards['price_min']
        )

    def _min_price_selected(self, update, context):
        chat_id = update.callback_query.message.chat_id
        min_price = re.search("\d+", update.callback_query.data).group(0)
        self._subscription_manager.update(chat_id, {"price_min": int(min_price)})
        update.callback_query.edit_message_text(
            messages.messages['price_max'],
            parse_mode=ParseMode.MARKDOWN_V2,
            reply_markup=messages.keyboards['price_max']
        )

    def _max_price_selected(self, update, context):
        chat_id = update.callback_query.message.chat_id
        max_price = re.search("\d+", update.callback_query.data).group(0)
        self._subscription_manager.update(chat_id, {"price_max": int(max_price)})
        update.callback_query.edit_message_text(messages.messages['configured'])

    @staticmethod
    def _district_back(update, context):
        update.callback_query.edit_message_text(
            messages.messages['start'],
            reply_markup=messages.keyboards['start']
        )

    @staticmethod
    def _min_price_back(update, context):
        update.callback_query.edit_message_text(
            messages.messages['district'],
            reply_markup=messages.keyboards['district']
        )

    @staticmethod
    def _max_price_back(update, context):
        update.callback_query.edit_message_text(
            messages.messages['price_min'],
            reply_markup=messages.keyboards['price_min']
        )

    def _poll_bazaraki(self):
        try:
            print(f"{datetime.now().strftime('%H:%M:%S')} polling www.bazaraki.com")
            updates = self._repo.get_updates(districts=District.values(), price_min=0, price_max=3200)
            print(f"{datetime.now().strftime('%H:%M:%S')} got {len(updates)} new ads")
            self._handle_updates(updates)
            time.sleep(self._timeout)
            self._poll_bazaraki()
        except Exception as e:
            print(f"{datetime.now().strftime('%H:%M:%S')} Error: {str(e)}")

    def _handle_updates(self, updates: List[Estate]):
        subscriptions = self._subscription_manager.subscriptions()
        for estate in updates:
            for subscription in subscriptions:
                price = int(float(estate.price))
                district = estate.district().value
                if price in range(subscription.price_min, subscription.price_max):
                    if district in subscription.districts:
                        self._updater.bot.send_message(
                            chat_id=subscription.id,
                            parse_mode=ParseMode.HTML,
                            text=estate.telegram_msg()
                        )
