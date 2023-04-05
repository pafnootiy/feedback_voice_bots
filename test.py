import argparse
import os
import json
from dotenv import load_dotenv
load_dotenv()
# file_with_phrases = os.getenv('FIlE_WITH_PHRASES')
# with open(file_with_phrases, "r", encoding="utf-8") as file:
#     phrases_json = file.read()
# print(file_with_phrases)

# path_to_phrases = os.getenv('FIlE_WITH_PHRASES')
# print(path_to_phrases)
# project_id = os.getenv("PROGECT_ID")
# session_id = os.getenv("TG_SESSION_ID")
# print(project_id)
# print(session_id)
# parser = argparse.ArgumentParser(
#     description='Описание что делает программа'
# )
# parser.add_argument('path_to_phrases', help='Ваше имя')
# args = parser.parse_args()
# print(args.path_to_phrases)

file_with_phrases = os.getenv('PATH_TO_FILE')
 
with open(file_with_phrases, "r", encoding="utf-8") as file:
    phrases_json = file.read()
phrases = json.loads(phrases_json)


print(phrases)
