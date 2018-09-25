import telebot
import find_info
import config

bot = telebot.TeleBot(config.bot_api)

markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
markup.row('/start', '/help', '/stop')
markup.row('Москва', 'Санкт-Петербург', 'Махачкала')
markup.row('Сочи', 'Екатеринбург', 'Краснодар')


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id,
                     'Привет! Напиши город и узнаешь информацию про него',
                     reply_markup=markup)


@bot.message_handler(commands=['stop'])
def handle_stop(message):
    bot.send_message(message.from_user.id,
                     'До свидания!',
                     reply_markup=telebot.types.ReplyKeyboardRemove())


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.from_user.id,
                     'Я могу помочь тебе узнать информацию про города России\n'
                     'Тебе нужно лишь отправить сообщение, в котором будет название города\n'
                     'Например, "Москва" или "Владивосток"',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        d = find_info.find(message.text)

        # print(d)

        bot.send_message(message.from_user.id,
                         'Порядок в списке городов: {0}\nГород: {1}\nРегион: {2}\nФедеральный округ: {3}\n'
                         'Население: {4}\nДата основания города: {5}'.format(d['list'], d['city'], d['reg'],
                                                                             d['federal'], d['people'], d['date']),
                         reply_markup=markup)
    except IndexError:
        bot.send_message(message.from_user.id,
                         'Вы ввели несуществующий город!',
                         reply_markup=markup)


@bot.message_handler(content_types=['sticker'])
def handle_text(message):
    bot.send_message(message.from_user.id,
                     'Друг, отправляй стикеры не мне!',
                     reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def handle_text(message):
    bot.send_message(message.from_user.id,
                     'Перестань отправлять мне фигню',
                     reply_markup=markup)


@bot.message_handler(content_types=['audio'])
def handle_text(message):
    bot.send_message(message.from_user.id,
                     'Я обещаю, что когда-нибудь сделаю нейросеть, которая будет понимать голосовую речь\n'
                     'А пока что перестань надо мной издеваться. Отправь текстовое сообщение',
                     reply_markup=markup)


@bot.message_handler(content_types=['document'])
def handle_text(message):
    bot.send_message(message.from_user.id,
                     'Хватит отправлять мне чушь!',
                     reply_markup=markup)


@bot.message_handler(content_types=['video'])
def handle_text(message):
    bot.send_message(message.from_user.id,
                     'Не отправляй мне глупости, человек!',
                     reply_markup=markup)


bot.polling(none_stop=True)
