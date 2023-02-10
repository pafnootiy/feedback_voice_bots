import json
from pprint import pprint
from google.cloud import dialogflow
import os
from dotenv import load_dotenv

project_id=os.getenv("PROGECT_ID")


with open ("training_phrases.json","r",encoding="utf-8") as file:
    phrases_json=file.read()
training_phrases = json.loads(phrases_json)

# pprint(phrases)


def get_serialized_pharases(training_phrases):
    display_name =[]
    questions =[]
    answers = []

 
    for title,issue in training_phrases.items():
        display_name.append(title)
        questions.append(issue['questions'])
        answers.append(issue['answer']) 
 
         
    return display_name,questions,answers

# display_name,questions,answers =get_serialized_pharases(training_phrases)
message_texts = "тест текст"
display_name ="тест дисплей"

def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    """Create an intent of the given intent type."""
    

    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    print("Intent created: {}".format(response))
create_intent(project_id, display_name, training_phrases, message_texts)
