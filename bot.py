import requests
import telegram
import os
from dotenv import load_dotenv
from telegram.ext import Updater, MessageHandler, Filters

from google.cloud import storage

from intents import detect_intent_texts


import logging

from telegram import Update, ForceReply,Message,Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from google.cloud import dialogflow_v2beta1 as dialogflow

 
load_dotenv()

tg_token=os.getenv("TG_API_TOKEN")
project_id=os.getenv("PROGECT_ID")
language_code=os.getenv("LANGUAGE_CODE")
session_id=os.getenv("SESSION_ID")

 

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
    user_massage =  update.message['text']
    update.message.reply_text(detect_intent_texts(user_massage, project_id, session_id, language_code))
 
updater = Updater(tg_token)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, bot_send_message))
updater.start_polling()

updater.idle()


 
