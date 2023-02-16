import os
import random 
import vk_api as vk
import logging


from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType
from intents import detect_intent_texts
from log_handlers import LogsHandler

logger = logging.getLogger(__file__)



def vk_bot_send_message(event, vk_api):
    project_id = os.getenv("PROGECT_ID")
    language_code = os.getenv("LANGUAGE_CODE")
    session_id = os.getenv("SESSION_ID")
    user_message = event.text
    vk_api.messages.send(
        user_id=event.user_id,
        message=detect_intent_texts(user_message, project_id, session_id,
                                    language_code),
        random_id=random.randint(1, 1000)
    )

def main():
    
    load_dotenv()

    logging.basicConfig(
         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    logs_handler = LogsHandler(level=logging.INFO)
    logger.addHandler(logs_handler)
    
    vk_token = os.getenv("VK_TOKEN")
    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            vk_bot_send_message(event, vk_api)

if __name__ == "__main__" :
    main()

