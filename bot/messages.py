from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from core.data.district import District

messages = {
    'start':
        u'Hi.\n\n'
        u'I will help you with finding property to rent in Cyprus!\n'
        u'Every 5 minutes I poll Bazaraki for new listings and send you the latest ones based on your search criteria.',

    'district': 'Let`s start with a district',

    'price_min': 'Please enter a *minimum* rent price 💶',

    'price_max': 'What about the *maximum* rent price? 💶',

    'configured':
        u'Ok!\n'
        u'I will send you updates based on this search criteria.\n'
        u'You can always change settings via /configure command.'
}

keyboards = {
    'configure': InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('⚙️ Configure Search Criteria', callback_data=str('district'))
            ]
        ]
    ),

    'district': InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('Paphos', callback_data=str('district ' + str(District.PAPHOS.value)))],
            [InlineKeyboardButton('Limassol', callback_data=str('district ' + str(District.LIMASSOL.value)))],
            [InlineKeyboardButton('Larnaka', callback_data=str('district ' + str(District.LARNACA.value)))],
            [InlineKeyboardButton('Lefkosia', callback_data=str('district ' + str(District.LEFKOSIA.value)))],
            [InlineKeyboardButton('Famagusta', callback_data=str('district ' + str(District.FAMAGUSTA.value)))],
            [InlineKeyboardButton('⬅️ Back', callback_data=str('back_district'))]
        ]
    ),

    'price_min': InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('400', callback_data=str('price_min ' + str(400))),
                InlineKeyboardButton('500', callback_data=str('price_min ' + str(500))),
                InlineKeyboardButton('600', callback_data=str('price_min ' + str(600))),
                InlineKeyboardButton('700', callback_data=str('price_min ' + str(700))),
                InlineKeyboardButton('800', callback_data=str('price_min ' + str(800))),
            ],
            [
                InlineKeyboardButton('900', callback_data=str('price_min ' + str(900))),
                InlineKeyboardButton('1000', callback_data=str('price_min ' + str(1000))),
                InlineKeyboardButton('1100', callback_data=str('price_min ' + str(1100))),
                InlineKeyboardButton('1200', callback_data=str('price_min ' + str(1200))),
            ],
            [
                InlineKeyboardButton('1300', callback_data=str('price_min ' + str(1300))),
                InlineKeyboardButton('1500', callback_data=str('price_min ' + str(1500))),
                InlineKeyboardButton('1700', callback_data=str('price_min ' + str(1700))),
                InlineKeyboardButton('2000', callback_data=str('price_min ' + str(2000))),
            ],
            [
                InlineKeyboardButton('2200', callback_data=str('price_min ' + str(2200))),
                InlineKeyboardButton('2500', callback_data=str('price_min ' + str(2500))),
                InlineKeyboardButton('2800', callback_data=str('price_min ' + str(2800))),
                InlineKeyboardButton('3200', callback_data=str('price_min ' + str(3200))),
            ],
            [
                InlineKeyboardButton('⬅️ Back', callback_data=str('back_price_min'))
            ]
        ]
    ),

    'price_max': InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('400', callback_data=str('price_max ' + str(400))),
                InlineKeyboardButton('500', callback_data=str('price_max ' + str(500))),
                InlineKeyboardButton('600', callback_data=str('price_max ' + str(600))),
                InlineKeyboardButton('700', callback_data=str('price_max ' + str(700))),
                InlineKeyboardButton('800', callback_data=str('price_max ' + str(800))),
            ],
            [
                InlineKeyboardButton('900', callback_data=str('price_max ' + str(900))),
                InlineKeyboardButton('1000', callback_data=str('price_max ' + str(1000))),
                InlineKeyboardButton('1100', callback_data=str('price_max ' + str(1100))),
                InlineKeyboardButton('1200', callback_data=str('price_max ' + str(1200))),
            ],
            [
                InlineKeyboardButton('1300', callback_data=str('price_max ' + str(1300))),
                InlineKeyboardButton('1500', callback_data=str('price_max ' + str(1500))),
                InlineKeyboardButton('1700', callback_data=str('price_max ' + str(1700))),
                InlineKeyboardButton('2000', callback_data=str('price_max ' + str(2000))),
            ],
            [
                InlineKeyboardButton('2200', callback_data=str('price_max ' + str(2200))),
                InlineKeyboardButton('2500', callback_data=str('price_max ' + str(2500))),
                InlineKeyboardButton('2800', callback_data=str('price_max ' + str(2800))),
                InlineKeyboardButton('3200', callback_data=str('price_max ' + str(3200))),
            ],
            [
                InlineKeyboardButton('⬅️ Back', callback_data=str('back_price_max'))
            ]
        ]
    ),
}
