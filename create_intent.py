import json
from pprint import pprint
import os
from dotenv import load_dotenv
load_dotenv()
from google.cloud import dialogflow


with open ("training_phrases.json","r",encoding="utf-8") as file:
    phrases_json=file.read()
phrases = json.loads(phrases_json)

# pprint(phrases)
project_id=os.getenv("PROGECT_ID")
display_name = "devman_training_phrases"
# message_texts = ["test","test2","test3"]



def create_intent(project_id, display_name, training_phrases_parts ):
    """Create an intent of the given intent type."""
     

    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)

    training_phrases = []
    for training_phrases_part,issue in training_phrases_parts.items():
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=[issue['answer']])
    message = dialogflow.Intent.Message(text=text)
    
    print(training_phrases)

        
    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )
 
    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )   #mvp
        
    print("Intent created: {}".format(response))

create_intent(project_id, display_name, phrases)


 