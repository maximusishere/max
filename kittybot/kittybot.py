from telebot import TeleBot

# Укажите токен, 
# который вы получили от @Botfather при создании бот-аккаунта:
bot = TeleBot(token='<token>')
# Укажите id своего аккаунта в Telegram:
chat_id = <chat_id>
message = 'Вам телеграмма!'
# Вызываем метод send_message, с помощью этого метода отправляются сообщения:
bot.send_message(chat_id, message)