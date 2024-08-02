import os
from dotenv import load_dotenv
from telebot import TeleBot, types
import requests

load_dotenv()

secret_token = os.getenv('TOKEN')

URL = os.getenv('URL')

bot = TeleBot(token=secret_token)

# Код запроса к thecatapi.com и обработку ответа обернём в функцию:


def get_new_image():
    try:
        response = requests.get(URL)
    except Exception as error:
        print(error)  
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)
    
    response = response.json()
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
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_newcat = types.KeyboardButton('/newcat')
    keyboard.add(button_newcat, row_width=3)

    bot.send_message(
        chat_id=chat.id,
        text=f'Привет, {name}. Посмотри, какого котика я тебе нашёл',
        reply_markup=keyboard,
    )

    bot.send_photo(chat.id, get_new_image())


@bot.message_handler(content_types=['text'])
def say_hi(message):
    chat = message.chat
    chat_id = chat.id
    bot.send_message(chat_id=chat_id, text='Привет, я KittyBot!')


bot.polling()
