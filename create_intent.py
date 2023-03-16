import json
import os

from dotenv import load_dotenv
from google.cloud import dialogflow


def create_intent(phrases, project_id):
    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project_id)

    for display_name, issue in phrases.items():
        training_phrases = []
        for phrase in issue["questions"]:
            part = dialogflow.Intent.TrainingPhrase.Part(text=phrase)
            training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
            training_phrases.append(training_phrase)

        text = dialogflow.Intent.Message.Text(text=[issue["answer"]])
        message = dialogflow.Intent.Message(text=text)

        intent = dialogflow.Intent(
            display_name=display_name, training_phrases=training_phrases,
            messages=[message]
        )
        response = intents_client.create_intent(
            request={"parent": parent, "intent": intent}
        )


def main():
    load_dotenv()
    path_to_phrases = os.getenv('PATH_TO_PHRASES')
    with open(path_to_phrases + "training_phrases.json", "r", encoding="utf-8") as file:
        phrases_json = file.read()
    phrases = json.loads(phrases_json)
    project_id = os.getenv("PROGECT_ID")
    create_intent(phrases, project_id)


if __name__ == "__main__":
    main()
