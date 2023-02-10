import requests
import telegram
import os
from dotenv import load_dotenv
from telegram.ext import Updater, MessageHandler, Filters

from google.cloud import storage

 

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


 
def detect_intent_texts(update: Update, context: CallbackContext):

    project_id = os.getenv("PROGECT_ID")
    language_code = os.getenv("LANGUAGE_CODE")
    session_id = os.getenv("SESSION_ID")  
    user_massage =  update.message['text']

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=user_massage,
                                      language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    
    print("=" * 20)
    print("Query text: {}".format(response.query_result.query_text))

 
    print("Fulfillment text: {}\n".format(
        response.query_result.fulfillment_text))

    update.message.reply_text(response.query_result.fulfillment_text)

  
 
updater = Updater(tg_token)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, detect_intent_texts))
updater.start_polling()

updater.idle()


 
