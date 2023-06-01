import logging
import os

import requests
from dotenv import load_dotenv
from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater

load_dotenv()
TELEGRAM_TOKEN = os.getenv('bot_token')
LOG_FILE = 'main.log'
LOG_FORMAT = '%(asctime)s, %(levelname)s, %(name)s, %(message)s'
logging.basicConfig(
    format=LOG_FORMAT,
    filename=LOG_FILE,
    level=logging.INFO,
)

URL = 'https://api.thecatapi.com/v1/images/search'

bot = Bot(token=TELEGRAM_TOKEN)

chat_id = os.getenv('chat_id')


def say_hi(update, context):
    chat = update.effective_chat
    send_message_params = {
        'chat_id': chat.id,
        'text': 'Привет, я KittyBot!'
    }
    context.bot.send_message(**send_message_params)


def get_new_image() -> str:
    try:
        response = requests.get(URL)
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)
    response = response.json()
    return response[0].get('url')


def new_cat(update, context):
    chat = update.effective_chat
    send_photo_params = {
        'chat_id': chat.id,
        'photo': get_new_image(),
    }
    context.bot.send_photo(**send_photo_params)


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['/newcat']], resize_keyboard=True)
    send_message_params = {
        'chat_id': chat.id,
        'text': f'Привет, {name}. Посмотри, какого котика я тебе нашёл',
        'reply_markup': button,
    }
    send_photo_params = {
        'chat_id': chat.id,
        'photo': get_new_image(),
    }
    context.bot.send_message(**send_message_params)
    context.bot.send_photo(**send_photo_params)


def main():
    updater = Updater(token=TELEGRAM_TOKEN)
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
