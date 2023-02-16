# feedback_voice_bots
## Бот-помощник для ответа на самые часто задаваемые вопросы

### Пример работы бота 
![bandicam 2023-02-16 06-20-38-470 (1)](https://user-images.githubusercontent.com/66752812/219253008-6d21b22d-5280-48a8-a693-1cccd8f0517a.gif)

Для тестирования Вы можете использовать ботов в TG: https://t.me/fd_dev_bot или в VK : https://vk.com/event41445255

## Подготовка к запуску

Для запуска сайта вам понадобится Python 3.0 и выше.

Скачайте код с GitHub. 

Установите вириуальное окружение в репозиторий

```sh
python -m venv venv
```
Активируйте его 
```sh
python venv/Scripts/activate
```
Установите зависимости:
```sh
pip install -r requirements.txt
```
## Добавьте переменные окружения 
Создайте файл .env со следующими переменными, где:

* TG_API_TOKEN=токен телеграмм бота  
* PROGECT_ID= ID проекта из json файла с ключами.  
* GOOGLE_APPLICATION_CREDENTIALS - путь к json файлу с ключами для DialogFlow. 
* DIALOG_FLOW_TOKEN = токен для DialogFlow 
* TG_CHAT_ID= чат id в телеграмме. 
* VK_TOKEN = токен группы в VK

Пример записи в файле .env

* TG_API_TOKEN=5969555759:AAFTmoRUfTq_ZHPPb0Ra0ulY3RtLvTwJ1mg
* PROGECT_ID=dvmn-project-gwll
* GOOGLE_APPLICATION_CREDENTIALS='C:\Users\Alex K\AppData\Roaming\gcloud\application_default_credentials.json'
* DIALOG_FLOW_TOKEN = AIzaSyBXHFF6JgELqzQLFBVmXCCeixgMp31deKY
* TG_CHAT_ID=230938172
* VK_TOKEN = vk1.a.QD-ChVpJV3HBTTmJJwtE5nDGA0VZkL82-0UWrDmTAwD9lYrw5XrCyFsro1ZiY8DXCZnUcKuwx-iE4CJE1H-fc-CMcCBVUu5e93xlT4nKdbjDUVaJ0OeqifkNzo3YZZkW2ggYPbhFnx7f4u3VEUZ-e-zDr4L-TmvNPzYBvOgmrO4b7OVyHW5SVXPdB1Z4gKCqsxcU6cSHnK7PSrbd3xTtUQ

## Запуск 
Для запуска бота в консоли введите следующие команды 

```sh
python tg_bot.py
```
```sh
python vk_bot.py
```
## Обучение бота 
 
Для обучения бота необходимо создать json файл с тренировочными фразами. Пример - training_phrases.json в корневой директории и запустить скрипт create_intent.py

```sh
python create_intent.py
```


## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
