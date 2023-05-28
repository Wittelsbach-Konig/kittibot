import os

from dotenv import load_dotenv
from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

load_dotenv()
TELEGRAM_TOKEN = os.getenv('bot_token')

bot = Bot(token=TELEGRAM_TOKEN)
updater = Updater(token=TELEGRAM_TOKEN)
chat_id = os.getenv('chat_id')


def say_hi(update, context):
    chat = update.effective_chat
    send_message_params = {
        'chat_id': chat.id,
        'text': 'Привет, я KittyBot!'
    }
    context.bot.send_message(**send_message_params)


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([
        ['Показать фото котика'],
        ['Который час?', 'Определи мой ip'],
        ['/random_digit'],
        ])
    send_message_params = {
        'chat_id': chat.id,
        'text': f'Спасибо, что включили меня {name}',
        'reply_markup': button,
    }
    context.bot.send_message(**send_message_params)


updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))
updater.start_polling()
updater.idle()


# if __name__ == '__main__':
# pass
# chat_id = os.getenv('chat_id')
# text = 'Вам телеграмма!'
# bot.send_message(chat_id, text)
