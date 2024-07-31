from pyrogram import Client

api_id = 26938862
api_hash = 'd1e3de1699413abc0a3244cc65c0a3a1'

# Создаём программный клиент, передаём в него
# имя сессии и данные для аутентификации в Client API
app = Client('my_account', api_id, api_hash)

app.start()
# Отправляем сообщение
# Первый параметр — это id чата (тип int) или имя получателя (тип str).
# Зарезервированное слово 'me' означает собственный аккаунт отправителя.
app.send_message(2011494322, 'Привет, это я!')
app.stop()