import vk_api
import os 
from dotenv import load_dotenv
load_dotenv()
import random

import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
from intents import detect_intent_texts 

 
vk_token =os.getenv("VK_TOKEN")
vk_session = vk_api.VkApi(token=vk_token)


tg_token = os.getenv("TG_API_TOKEN")
project_id = os.getenv("PROGECT_ID")
language_code = os.getenv("LANGUAGE_CODE")
session_id = os.getenv("SESSION_ID") 

def vk_bot_send_message(event, vk_api):
    user_message = event.text
    vk_api.messages.send(
        user_id=event.user_id,
        message= detect_intent_texts(user_message, project_id, session_id, language_code) ,
        random_id=random.randint(1,1000)
    )
 
 
vk_session = vk.VkApi(token=vk_token)
vk_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        vk_bot_send_message(event, vk_api)
