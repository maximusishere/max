import os
import logging
import asyncio
import time
import re
from datetime import datetime
from functools import wraps
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import ollama
from dotenv import load_dotenv
import nest_asyncio

load_dotenv()
nest_asyncio.apply()


# Конфигурация
class Config:
    TOKEN = os.getenv('TOKEN')
    MODEL_NAME = 'deepseek-r1:7b'
    MAX_CONTEXT_LENGTH = 12
    REQUEST_INTERVAL = 1  # seconds
    SYSTEM_PROMPT = """Ты - умный помощник, который отвечает на русском языке. 
    Будь вежливым, информативным и старайся давать развернутые ответы. 
    Если вопрос непонятен - уточни. 
    Если нужно - задавай уточняющие вопросы."""
    LOG_FILE = 'user_chats.log'  # Файл для сохранения переписки


# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)

if not Config.TOKEN:
    logging.error("Токен бота не найден! Проверьте .env или укажите токен в коде.")
    exit(1)


# Обработчик ошибок
def error_handler(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {e}", exc_info=True)
            if len(args) > 0 and isinstance(args[0], Update):
                await args[0].message.reply_text('Произошла ошибка. Пожалуйста, попробуйте позже.')

    return wrapper


def save_chat_to_file(user_id: int, username: str, user_message: str, bot_response: str):
    """Сохраняет переписку пользователя с ботом в файл"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(Config.LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"Дата/время: {timestamp}\n")
        f.write(f"Пользователь: {username} (ID: {user_id})\n")
        f.write(f"Сообщение пользователя: {user_message}\n")
        f.write(f"Ответ бота: {bot_response}\n")
        f.write("-" * 50 + "\n\n")


class UserContext:
    def __init__(self, max_length=8):
        self.contexts = {}
        self.max_length = max_length

    def init_chat(self, user_id):
        if user_id not in self.contexts:
            self.contexts[user_id] = [
                {'role': 'system', 'content': Config.SYSTEM_PROMPT}
            ]

    def add_message(self, user_id, role, content):
        self.init_chat(user_id)
        self.contexts[user_id].append({'role': role, 'content': content})
        self.contexts[user_id] = self.contexts[user_id][-self.max_length:]

    def get_context(self, user_id):
        self.init_chat(user_id)
        return self.contexts[user_id]


user_context = UserContext(max_length=Config.MAX_CONTEXT_LENGTH)


class OllamaClient:
    def __init__(self):
        self.last_request_time = 0

    async def get_response(self, messages):
        current_time = time.time()
        elapsed = current_time - self.last_request_time
        if elapsed < Config.REQUEST_INTERVAL:
            await asyncio.sleep(Config.REQUEST_INTERVAL - elapsed)

        self.last_request_time = time.time()
        try:
            response = ollama.chat(
                model=Config.MODEL_NAME,
                messages=messages,
                options={
                    'temperature': 0.7,  # добавляет вариативность ответов (0-1)
                    'num_ctx': 4096,  # увеличиваем контекстное окно
                }
            )
            # Удаляем теги <think> и их содержимое
            clean_response = re.sub(r'<think>.*?</think>', '', response['message']['content'], flags=re.DOTALL)
            return clean_response.strip()
        except Exception as e:
            logging.error(f"Ollama error: {e}")
            raise


ollama_client = OllamaClient()


# Обработчики команд
@error_handler
async def start(update: Update, context) -> None:
    user = update.effective_user
    logging.info(f"New user started chat: {user.full_name} (ID: {user.id})")
    await update.message.reply_text('Привет. Я могу ответить на ваши вопросы.')


@error_handler
async def handle_message(update: Update, context):
    user = update.effective_user
    user_id = user.id
    username = user.full_name
    message_text = update.message.text

    # Логируем полученное сообщение
    logging.info(f"Message from {username} (ID: {user_id}): {message_text}")

    user_context.add_message(user_id, 'user', message_text)
    messages = user_context.get_context(user_id)

    response_text = await ollama_client.get_response(messages)
    user_context.add_message(user_id, 'assistant', response_text)

    # Сохраняем переписку в файл
    save_chat_to_file(user_id, username, message_text, response_text)

    # Логируем ответ бота
    logging.info(f"Bot response to {username}: {response_text}")

    await update.message.reply_text(response_text)


async def main() -> None:
    application = ApplicationBuilder().token(Config.TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Создаем файл для логов, если его нет
    if not os.path.exists(Config.LOG_FILE):
        with open(Config.LOG_FILE, 'w', encoding='utf-8') as f:
            f.write("Лог переписки пользователей с ботом\n")
            f.write("=" * 50 + "\n\n")

    await application.run_polling()


if __name__ == '__main__':
    asyncio.run(main())