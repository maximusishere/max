from telebot import TeleBot
import requests


bot = TeleBot(token='1659639915:AAHLGCTJMVCBPqtTid2Mi-rpuHBu6IISew0')

URL = 'https://api.thecatapi.com/v1/images/search'

# Код запроса к thecatapi.com и обработку ответа обернём в функцию:
def get_new_image():
    response = requests.get(URL).json()
    random_cat = response[0].get('url')
    return random_cat


# Добавляем хендлер для команды /newcat:
@bot.message_handler(commands=['newcat'])
def new_cat(message):
    chat = message.chat
    bot.send_photo(chat.id, get_new_image())


@bot.message_handler(commands=['start'])
def wake_up(message):
    chat = message.chat
    name = message.chat.first_name

    bot.send_message(
        chat_id=chat.id,
        text=f'Привет, {name}. Посмотри, какого котика я тебе нашёл',
    )

    bot.send_photo(chat.id, get_new_image())


@bot.message_handler(content_types=['text'])
def say_hi(message):
    chat = message.chat
    chat_id = chat.id
    bot.send_message(chat_id=chat_id, text='Привет, я KittyBot!')

bot.polling()
# chat_id = 1669837246
# message = 'Вам телеграмма!'
# # Вызываем метод send_message, с помощью этого метода отправляются сообщения:
# bot.send_message(chat_id, message)

# @bot.message_handler(commands=['start'])
# def wake_up(message):
#     chat = message.chat
#     name = chat.first_name
#     chat_id = chat.id
#     bot.send_message(chat_id=chat_id, text=f'Спасибо, что включили меня, {name}!')

# @bot.message_handler(content_types=['text'])
# def say_hi(message):
#     chat = message.chat
#     chat_id = chat.id
#     bot.send_message(chat_id=chat_id, text='Привет, я Kittybot!')
URL = 'https://api.thecatapi.com/v1/images/search'
response = requests.get(URL).json()

print(response)

# response — это список. Удостоверимся:
print(type(response))

# Какой длины список response?
print(len(response))

# Посмотрим, какого типа первый элемент:
print(type(response[0]))

# chat_id = 1669837246
# text = 'Вам телеграмма!'
# # Отправка сообщения
# bot.send_message(chat_id, text)
# # Отправка изображения
# bot.send_photo(chat_id, URL)



# bot.polling()
