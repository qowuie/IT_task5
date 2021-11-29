import telebot
from telebot import types
import random

token = "2121829809:AAHBY9kMVcI831kMqiacwmJ8cuYI8O1Sm8o"

bot = telebot.TeleBot(token)

cat_list = [
    'https://static.ngs.ru/news/2021/99/preview/027344c0e96f7237500e48199537fce801149630_659_439_c.jpg',
    'https://cdnimg.rg.ru/img/content/190/36/72/kinopoisk.ru-A-Street-Cat-Named-Bob-2889441_d_850.jpg',
    'https://static.wikia.nocookie.net/fallout/images/f/fc/FO4HRTP_Cat.png/revision/latest?cb=20200829105031&path-prefix=ru',
    'https://icdn.lenta.ru/images/2020/07/13/16/20200713161106967/square_320_4dd6db2859b29f4b1ba2d684155a5cc6.png',
    'https://upload.wikimedia.org/wikipedia/commons/0/0e/Felis_silvestris_silvestris.jpg',
]

exercises_gifs = {
    'Приседания с поворотом корпуса': 'https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D1%80%D0%B8%D1%81%D0%B5%D0%B4-%D1%81-%D0%BF%D0%BE%D0%B2%D0%BE%D1%80%D0%BE%D1%82%D0%BE%D0%BC-%D0%BA%D0%BE%D1%80%D0%BF%D1%83%D1%81%D0%B0.gif',
    'Червяк с отжиманием': 'https://makefitness.pro/wp-content/uploads/2020/02/%D1%87%D0%B5%D1%80%D0%B2%D1%8F%D0%BA-%D1%81-%D0%BE%D1%82%D0%B6%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D0%B5%D0%BC.gif',
    'Армейские отжимания': 'https://makefitness.pro/wp-content/uploads/2020/02/%D0%B0%D1%80%D0%BC%D0%B5%D0%B9%D1%81%D0%BA%D0%B8%D0%B5-%D0%BE%D1%82%D0%B6%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D1%8F.gif',
    'Упражнение пловец': 'https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D0%BB%D0%BE%D0%B2%D0%B5%D1%86-%D0%BB%D0%B5%D0%B6%D0%B0-%D0%BD%D0%B0-%D0%B6%D0%B8%D0%B2%D0%BE%D1%82%D0%B5.gif',
    'Упражнение "книжка"': 'https://makefitness.pro/wp-content/uploads/2020/02/%D0%BA%D0%BD%D0%B8%D0%B6%D0%BA%D0%B0-2.gif',
    'Поднос колена сбоку в упоре': 'https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D0%BE%D0%B4%D0%BD%D0%BE%D1%81-%D0%BA%D0%BE%D0%BB%D0%B5%D0%BD%D0%B0-%D1%81%D0%B1%D0%BE%D0%BA%D1%83-%D0%B2-%D1%83%D0%BF%D0%BE%D1%80%D0%B5.gif',
    'Классические подтягивания': 'https://makefitness.pro/wp-content/uploads/2020/02/%D0%9F%D0%BE%D0%B4%D1%82%D1%8F%D0%B3%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D1%88%D0%B8%D1%80%D0%BE%D0%BA%D0%B8%D0%BC-%D1%85%D0%B2%D0%B0%D1%82%D0%BE%D0%BC.gif',
    'Отжимания': 'https://makefitness.pro/wp-content/uploads/2020/02/%D0%BE%D1%82%D0%B6%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B8%D0%BA.gif',
    'Подтягивания обратным хватом': 'https://makefitness.pro/wp-content/uploads/2020/02/%D0%9F%D0%BE%D0%B4%D1%82%D1%8F%D0%B3%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BE%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D1%8B%D0%BC-%D1%85%D0%B2%D0%B0%D1%82%D0%BE%D0%BC.gif',
    'Отжимания спиной к стулу': 'https://makefitness.pro/wp-content/uploads/2020/02/%D0%BE%D1%82%D0%B6%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D1%8F-%D1%81%D0%BF%D0%B8%D0%BD%D0%BE%D0%B9-%D0%BA-%D1%81%D0%BA%D0%B0%D0%BC%D1%8C%D0%B5.gif',
    'Упражнение на пресс': 'https://makefitness.pro/wp-content/uploads/2020/02/%D0%BA%D0%BD%D0%B8%D0%B6%D0%BA%D0%B0-2.gif',
    'Приседания плие с гантелей': 'https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D1%80%D0%B8%D1%81%D0%B5%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D0%BB%D0%B8%D0%B5-%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D1%8F%D0%BC%D0%B8.gif',
    'Тяга гантель в наклоне': 'https://makefitness.pro/wp-content/uploads/2020/02/%D1%82%D1%8F%D0%B3%D0%B0-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D0%B2-%D0%BD%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5.gif',
    'Жим гантель лежа': 'https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D0%BB%D1%91%D0%B6%D0%B0-1.gif',
    'Махи с гантелями стоя': 'https://makefitness.pro/wp-content/uploads/2020/02/%D0%BC%D0%B0%D1%85%D0%B8-%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D1%8F%D0%BC%D0%B8-%D1%81%D1%82%D0%BE%D1%8F.gif',
    'Подъем гантель на бицепс': 'https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D0%BE%D0%B4%D1%8A%D1%91%D0%BC-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D0%BD%D0%B0-%D0%B1%D0%B8%D1%86%D0%B5%D0%BF%D1%81-%D1%81-%D1%81%D1%83%D0%BF%D0%B8%D0%BD%D0%B0%D1%86%D0%B8%D0%B5%D0%B9.gif',
    'Французский жим сидя': 'https://makefitness.pro/wp-content/uploads/2020/02/%D1%84%D1%80%D0%B0%D0%BD%D1%86%D1%83%D0%B7%D0%BA%D0%B8%D0%B9-%D0%B6%D0%B8%D0%BC-%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D1%81%D0%B8%D0%B4%D1%8F.gif',
    'Жим штанги лежа': 'https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%B8-%D0%BB%D0%B5%D0%B6%D0%B0.gif',
    'Тяга штанги в наклоне': 'https://makefitness.pro/wp-content/uploads/2020/02/%D1%82%D1%8F%D0%B3%D0%B0-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%B8-%D0%B2-%D0%BD%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD%D0%B52.gif',
    'Жим штанги стоя': 'https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%B8-%D1%81%D1%82%D0%BE%D1%8F.gif',
    'Подъем штанги на бицепс': 'https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D0%BE%D0%B4%D1%8A%D0%B5%D0%BC-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%B8-%D0%BD%D0%B0-%D0%B1%D0%B8%D1%86%D0%B5%D0%BF%D1%81.gif',
}

exercises_text = {
    'нет': '''
*Упражнения для всего тела без инвентаря*
1\\. Приседания с поворотом корпуса
2\\. Червяк с отжиманием
3\\. Армейские отжимания
4\\. Упражнение пловец
5\\. Упражнение "книжка"
6\\. Поднос колена сбоку в упоре

*Кол\\-во рабочих подходов в упражнении: 2\\-3*
*Кол\\-во повторений: 10\\-15 \\(или больше, если сможете\\)*
*Отдых между подходами: 2\\-3 минуты*
''',
    'турник': '''
*Упражнения для всего тела с турником*
1\\. Классические подтягивания
2\\. Отжимания
3\\. Подтягивания обратным хватом
4\\. Отжимания спиной к стулу
5\\. Упражнение на пресс

*Кол\\-во рабочих подходов в упражнении: 2\\-3*
*Кол\\-во повторений: 10\\-15 \\(в отжиманиях \\- на максимум\\)*
*Отдых между подходами: 2\\-3 минуты*

*Нагрузка подбирается в зависимости от ваших физических данных*
''',
    'гантели': '''
*Упражнения для всего тела с гантелями*
1\\. Приседания плие с гантелей
2\\. Тяга гантель в наклоне
3\\. Жим гантель лежа
4\\. Махи с гантелями стоя
5\\. Подъем гантель на бицепс
6\\. Французский жим сидя
7\\. Упражнение на пресс

*Кол\\-во рабочих подходов в упражнении: 2\\-3*
*Кол\\-во повторений: 10\\-15*
*Отдых между подходами: 2\\-3 минуты*

*Рабочий вес подбирается в зависимости от ваших физических данных*
''',
    'штанга': '''
*Упражнения для всего тела со штангой*
1\\. Приседания со штангой
2\\. Жим штанги лежа
3\\. Тяга штанги в наклоне
4\\. Жим штанги стоя
5\\. Подъем штанги на бицепс
6\\. Французский жим сидя

*Кол\\-во рабочих подходов в упражнении: 2\\-3*
*Кол\\-во повторений: 10\\-15*
*Отдых между подходами: 2\\-3 минуты*

*Рабочий вес подбирается в зависимости от ваших физических данных*
''',

}


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help", "Тренировка", "Упражнения", "Мотивация")
    bot.send_message(message.chat.id, 'Привет!',
                     reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею:\nМотивировать, если нажать кнопку "мотивация"\nЕсли хочите '
                                      'потренироваться, нажмите кнопку "тренировка"\n'
                                      'Если какое-нибудь упражнение непонятно, нажмите "упражнения"')


@bot.message_handler(content_types=['text'])
def answer(message):
    text = message.text.lower()
    if text == "упражнения":
        markup = types.InlineKeyboardMarkup()

        prised = types.InlineKeyboardButton('Приседания с поворотом корпуса',
                                            callback_data='Приседания с поворотом корпуса')
        worm = types.InlineKeyboardButton('Червяк с отжиманием', callback_data='Червяк с отжиманием')
        military_pushups = types.InlineKeyboardButton('Армейские отжимания', callback_data='Армейские отжимания')
        plovec = types.InlineKeyboardButton('Упражнение пловец', callback_data='Упражнение пловец')
        book = types.InlineKeyboardButton('Упражнение "книжка"', callback_data='Упражнение "книжка"')
        podnos = types.InlineKeyboardButton('Поднос колена сбоку в упоре', callback_data='Поднос колена сбоку в упоре')
        classic_pullups = types.InlineKeyboardButton('Классические подтягивания',
                                                     callback_data='Классические подтягивания')
        pushups = types.InlineKeyboardButton('Отжимания', callback_data='Отжимания')
        reserved_pullups = types.InlineKeyboardButton('Подтягивания обратным хватом',
                                                      callback_data='Подтягивания обратным хватом')
        back_pushups = types.InlineKeyboardButton('Отжимания спиной к стулу', callback_data='Отжимания спиной к стулу')
        abs = types.InlineKeyboardButton('Упражнение на пресс', callback_data='Упражнение на пресс')
        plie = types.InlineKeyboardButton('Приседания плие с гантелей', callback_data='Приседания плие с гантелей')
        tyaga_ganteli = types.InlineKeyboardButton('Тяга гантель в наклоне', callback_data='Тяга гантель в наклоне')
        bench_dumbbells = types.InlineKeyboardButton('Жим гантель лежа', callback_data='Жим гантель лежа')
        mahi_dumbbells = types.InlineKeyboardButton('Махи с гантелями стоя', callback_data='Махи с гантелями стоя')
        up_dumbbells = types.InlineKeyboardButton('Подъем гантель на бицепс', callback_data='Подъем гантель на бицепс')
        french = types.InlineKeyboardButton('Французский жим сидя', callback_data='Французский жим сидя')
        bench_horiz = types.InlineKeyboardButton('Жим штанги лежа', callback_data='Жим штанги лежа')
        tyaga_horiz = types.InlineKeyboardButton('Тяга штанги в наклоне', callback_data='Тяга штанги в наклоне')
        stay_horiz = types.InlineKeyboardButton('Жим штанги стоя', callback_data='Жим штанги стоя')
        up_biceps = types.InlineKeyboardButton('Подъем штанги на бицепс', callback_data='Подъем штанги на бицепс')

        markup.row(prised)
        markup.row(worm)
        markup.row(military_pushups)
        markup.row(plovec)
        markup.row(book)
        markup.row(podnos)
        markup.row(classic_pullups)
        markup.row(pushups)
        markup.row(reserved_pullups)
        markup.row(back_pushups)
        markup.row(abs)
        markup.row(plie)
        markup.row(tyaga_ganteli)
        markup.row(bench_dumbbells)
        markup.row(mahi_dumbbells)
        markup.row(up_dumbbells)
        markup.row(bench_horiz)
        markup.row(tyaga_horiz)
        markup.row(stay_horiz)
        markup.row(up_biceps)
        markup.row(french)

        bot.send_message(message.chat.id, 'Выберите непонятные упражнения', reply_markup=markup)

    if text == "тренировка":
        markup = types.InlineKeyboardMarkup()

        without_equipment = types.InlineKeyboardButton('Нет инвертаря', callback_data='нет')
        horizontal_bar = types.InlineKeyboardButton('Есть турник', callback_data='турник')
        barbell = types.InlineKeyboardButton('Есть штанга', callback_data='штанга')
        dumbbells = types.InlineKeyboardButton('Есть гантели', callback_data='гантели')

        markup.row(without_equipment, horizontal_bar)
        markup.row(dumbbells, barbell)

        bot.send_message(message.chat.id, 'Какой инвентарь у тебя есть?', reply_markup=markup)

    if text == "мтуси":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    if 'кот' in text or 'кошк' in text:
        bot.send_photo(message.chat.id, random.choice(cat_list))
    if text == 'git':
        bot.send_message(message.chat.id, 'Ссылка на мой git: https://github.com/qowuie')
    if text == 'мотивация':
        bot.send_video(message.chat.id,
                       'https://psv4.userapi.com/c520036/u184705234/docs/d23/c3b9ef323ca3/7019747322506579201.gif?extra=q32yJ23LETNb2u4WjcQ1ZL8eJCbEI0LgiTYSnp-PJ9gG6PfuajSnSEUbKmD-TT06M9Nb2BiPcLQYEE6IRfomPTVU0pQagjmzxkiEwkDP7eVZLalCGrGDOLJaHpQwhPIG9xhCbNILiijLXungfr4FrbUrTA')


@bot.callback_query_handler(func=lambda call: True)
def handle(call):
    if call.message.text == 'Какой инвентарь у тебя есть?':
        bot.send_message(call.message.chat.id, exercises_text[str(call.data)], parse_mode='MarkdownV2')
    elif call.message.text == 'Выберите непонятные упражнения':
        bot.send_video(call.message.chat.id, exercises_gifs[str(call.data)], caption=call.data)
    bot.answer_callback_query(call.id)


if __name__ == "__main__":
    bot.infinity_polling()
