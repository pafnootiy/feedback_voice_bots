import vk_api
import os 
from dotenv import load_dotenv
load_dotenv()
vk_token =os.getenv("VK_TOKEN")
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token=vk_token)

longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Новое сообщение:')
        if event.to_me:
            print('Для меня от: ', event.user_id)
        else:
            print('От меня для: ', event.user_id)
        print('Текст:', event.text)