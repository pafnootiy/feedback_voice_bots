import os
import logging
import telegram
import sys
import requests


from dotenv import load_dotenv
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, \
    CallbackContext

from intents import detect_intent_texts
from log_handlers import LogsHandler


logger = logging.getLogger(__file__)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Привет {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def bot_send_message(update: Update, context: CallbackContext):
    project_id = os.getenv("PROGECT_ID")
    language_code = os.getenv("LANGUAGE_CODE")
    session_id = os.getenv("SESSION_ID")
    user_massage = update.message['text']
    update.message.reply_text(
        detect_intent_texts(user_massage, project_id, session_id,
                            language_code))


def main():
    load_dotenv()
    tg_token = os.getenv("TG_API_TOKEN")

    logging.basicConfig(
         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    logs_handler = LogsHandler(level=logging.INFO)
    logger.addHandler(logs_handler)
    logger.warning('Бот запущен!')
    
    try:
        updater = Updater(tg_token)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(
            MessageHandler(Filters.text & ~Filters.command, bot_send_message))
        updater.start_polling()
        updater.idle()
    except requests.exceptions.ConnectionError:

        print("Ошибка соединения", file=sys.stderr)
        logger.error('Ошибка соединения')

if __name__ == "__main__" :
    main()
