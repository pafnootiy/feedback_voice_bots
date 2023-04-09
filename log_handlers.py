import os
import logging
import telegram


class LogsHandler(logging.Handler):

    def __init__(self, level):
        self.bot_token = os.getenv('TG_API_TOKEN')
        self.chat_id = os.getenv('TG_CHAT_ID')
        self.bot = telegram.Bot(token=self.bot_token)
        super().__init__(level)

    def emit(self, record):
        log_entry = self.format(record)
        self.bot.send_message(text=log_entry, chat_id=self.chat_id)