from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from api.district import District

messages = {
    'start':
        u'Hi.\n\n'
        u'I will make your life easier by performing the search routine for you. 🤖\n'
        u'Every 5 minutes I poll Bazaraki for new listings and send you the latest ones based on your search criteria.\n\n'
        u'Hope you enjoy it. 🤍\n\n'
        u'For developers:\n'
        u'Feel free to contribute on <a href="https://github.com/lounah/bazaraki-scrapper-bot">github</a>',

    'district': 'Ok. Let`s start with a <strong>district</strong>',

    'price_min': 'Nice! What about a <strong>minimum</strong> price 💶?',

    'price_max': 'Ooookey, what about the <strong>maximum</strong> price? 💶',

    'car_query':
        u'What kind of car are you looking for?'
        u'Enter the search query (e.g. <strong>bmw x5 2004</strong>)',

    'configured':
        u'Cool!\n'
        u'I will send you updates based on this search criteria.\n'
        u'You can manage subscription via /subscription command.',

    'support': 'What happened? Please contact @lounvhx for troubleshooting.',

    'unsubscribe':
        u'Ok.\n'
        u'I`ve removed your subscriptions.\n'
        u'How do you rate user experience of this bot? For feedback please contact @lounvhx.'
}

keyboards = {
    'start': InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('🏘️️ Search for apartments to rent', callback_data=str('houses_search'))],
            [InlineKeyboardButton('🚗️ Search for cars', callback_data=str('cars_search'))]
        ]
    ),

    'subscriptions_manage': InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('⚙️ Manage', callback_data=str('subscriptions_manage')),
            ]
        ]
    ),

    'houses_districts': InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('Paphos', callback_data=str('houses_district ' + str(District.PAPHOS.value)))],
            [InlineKeyboardButton('Limassol', callback_data=str('houses_district ' + str(District.LIMASSOL.value)))],
            [InlineKeyboardButton('Larnaka', callback_data=str('houses_district ' + str(District.LARNACA.value)))],
            [InlineKeyboardButton('Lefkosia', callback_data=str('houses_district ' + str(District.LEFKOSIA.value)))],
            [InlineKeyboardButton('Famagusta', callback_data=str('houses_district ' + str(District.FAMAGUSTA.value)))],
            [InlineKeyboardButton('⬅️ Back', callback_data=str('houses_district_back'))]
        ]
    ),

    'cars_districts': InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('Paphos', callback_data=str('cars_district ' + str(District.PAPHOS.value)))],
            [InlineKeyboardButton('Limassol', callback_data=str('cars_district ' + str(District.LIMASSOL.value)))],
            [InlineKeyboardButton('Larnaka', callback_data=str('cars_district ' + str(District.LARNACA.value)))],
            [InlineKeyboardButton('Lefkosia', callback_data=str('cars_district ' + str(District.LEFKOSIA.value)))],
            [InlineKeyboardButton('Famagusta', callback_data=str('cars_district ' + str(District.FAMAGUSTA.value)))],
            [InlineKeyboardButton('⬅️ Back', callback_data=str('cars_district_back'))]
        ]
    ),

    'houses_price_min': InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('400', callback_data=str('houses_price_min ' + str(400))),
                InlineKeyboardButton('500', callback_data=str('houses_price_min ' + str(500))),
                InlineKeyboardButton('600', callback_data=str('houses_price_min ' + str(600))),
                InlineKeyboardButton('700', callback_data=str('houses_price_min ' + str(700))),
                InlineKeyboardButton('800', callback_data=str('houses_price_min ' + str(800))),
            ],
            [
                InlineKeyboardButton('900', callback_data=str('houses_price_min ' + str(900))),
                InlineKeyboardButton('1000', callback_data=str('houses_price_min ' + str(1000))),
                InlineKeyboardButton('1100', callback_data=str('houses_price_min ' + str(1100))),
                InlineKeyboardButton('1200', callback_data=str('houses_price_min ' + str(1200))),
            ],
            [
                InlineKeyboardButton('1300', callback_data=str('houses_price_min ' + str(1300))),
                InlineKeyboardButton('1500', callback_data=str('houses_price_min ' + str(1500))),
                InlineKeyboardButton('1700', callback_data=str('houses_price_min ' + str(1700))),
                InlineKeyboardButton('2000', callback_data=str('houses_price_min ' + str(2000))),
            ],
            [
                InlineKeyboardButton('2200', callback_data=str('houses_price_min ' + str(2200))),
                InlineKeyboardButton('2500', callback_data=str('houses_price_min ' + str(2500))),
                InlineKeyboardButton('2800', callback_data=str('houses_price_min ' + str(2800))),
                InlineKeyboardButton('3200', callback_data=str('houses_price_min ' + str(3200))),
            ],
            [
                InlineKeyboardButton('⬅️ Back', callback_data=str('houses_price_min_back'))
            ]
        ]
    ),

    'houses_price_max': InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('400', callback_data=str('houses_price_max ' + str(400))),
                InlineKeyboardButton('500', callback_data=str('houses_price_max ' + str(500))),
                InlineKeyboardButton('600', callback_data=str('houses_price_max ' + str(600))),
                InlineKeyboardButton('700', callback_data=str('houses_price_max ' + str(700))),
                InlineKeyboardButton('800', callback_data=str('houses_price_max ' + str(800))),
            ],
            [
                InlineKeyboardButton('900', callback_data=str('houses_price_max ' + str(900))),
                InlineKeyboardButton('1000', callback_data=str('houses_price_max ' + str(1000))),
                InlineKeyboardButton('1100', callback_data=str('houses_price_max ' + str(1100))),
                InlineKeyboardButton('1200', callback_data=str('houses_price_max ' + str(1200))),
            ],
            [
                InlineKeyboardButton('1300', callback_data=str('houses_price_max ' + str(1300))),
                InlineKeyboardButton('1500', callback_data=str('houses_price_max ' + str(1500))),
                InlineKeyboardButton('1700', callback_data=str('houses_price_max ' + str(1700))),
                InlineKeyboardButton('2000', callback_data=str('houses_price_max ' + str(2000))),
            ],
            [
                InlineKeyboardButton('2200', callback_data=str('houses_price_max ' + str(2200))),
                InlineKeyboardButton('2500', callback_data=str('houses_price_max ' + str(2500))),
                InlineKeyboardButton('2800', callback_data=str('houses_price_max ' + str(2800))),
                InlineKeyboardButton('3200', callback_data=str('houses_price_max ' + str(3200))),
            ],
            [
                InlineKeyboardButton('⬅️ Back', callback_data=str('houses_price_max_back'))
            ]
        ]
    ),

    'cars_price_min': InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('1200', callback_data=str('cars_price_min ' + str(1200))),
                InlineKeyboardButton('1500', callback_data=str('cars_price_min ' + str(1500))),
                InlineKeyboardButton('1700', callback_data=str('cars_price_min ' + str(1700))),
                InlineKeyboardButton('2000', callback_data=str('cars_price_min ' + str(2000))),
                InlineKeyboardButton('2500', callback_data=str('cars_price_min ' + str(2500))),
            ],
            [
                InlineKeyboardButton('4000', callback_data=str('cars_price_min ' + str(4000))),
                InlineKeyboardButton('4300', callback_data=str('cars_price_min ' + str(4300))),
                InlineKeyboardButton('4800', callback_data=str('cars_price_min ' + str(4800))),
                InlineKeyboardButton('5000', callback_data=str('cars_price_min ' + str(5000))),
            ],
            [
                InlineKeyboardButton('5000', callback_data=str('cars_price_min ' + str(5000))),
                InlineKeyboardButton('6000', callback_data=str('cars_price_min ' + str(6000))),
                InlineKeyboardButton('7000', callback_data=str('cars_price_min ' + str(7000))),
                InlineKeyboardButton('8000', callback_data=str('cars_price_min ' + str(8000))),
            ],
            [
                InlineKeyboardButton('10000', callback_data=str('cars_price_min ' + str(10000))),
                InlineKeyboardButton('15000', callback_data=str('cars_price_min ' + str(15000))),
                InlineKeyboardButton('19000', callback_data=str('cars_price_min ' + str(19000))),
                InlineKeyboardButton('25000', callback_data=str('cars_price_min ' + str(25000))),
            ],
            [
                InlineKeyboardButton('⬅️ Back', callback_data=str('cars_price_min_back'))
            ]
        ]
    ),

    'cars_price_max': InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('3000', callback_data=str('cars_price_max ' + str(3000))),
                InlineKeyboardButton('3400', callback_data=str('cars_price_max ' + str(3400))),
                InlineKeyboardButton('3800', callback_data=str('cars_price_max ' + str(3800))),
                InlineKeyboardButton('4200', callback_data=str('cars_price_max ' + str(4200))),
                InlineKeyboardButton('4600', callback_data=str('cars_price_max ' + str(4600))),
            ],
            [
                InlineKeyboardButton('5500', callback_data=str('cars_price_max ' + str(5500))),
                InlineKeyboardButton('6000', callback_data=str('cars_price_max ' + str(6000))),
                InlineKeyboardButton('7000', callback_data=str('cars_price_max ' + str(7000))),
                InlineKeyboardButton('8000', callback_data=str('cars_price_max ' + str(8000))),
            ],
            [
                InlineKeyboardButton('8500', callback_data=str('cars_price_max ' + str(8500))),
                InlineKeyboardButton('9500', callback_data=str('cars_price_max ' + str(9500))),
                InlineKeyboardButton('11000', callback_data=str('cars_price_max ' + str(11000))),
                InlineKeyboardButton('14000', callback_data=str('cars_price_max ' + str(14000))),
            ],
            [
                InlineKeyboardButton('17000', callback_data=str('cars_price_max ' + str(17000))),
                InlineKeyboardButton('21000', callback_data=str('cars_price_max ' + str(21000))),
                InlineKeyboardButton('28000', callback_data=str('cars_price_max ' + str(28000))),
                InlineKeyboardButton('35000', callback_data=str('cars_price_max ' + str(35000))),
            ],
            [
                InlineKeyboardButton('⬅️ Back', callback_data=str('cars_price_max_back'))
            ]
        ]
    ),
}
