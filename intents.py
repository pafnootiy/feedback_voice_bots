import os

from dotenv import load_dotenv
from google.cloud import dialogflow


def detect_intent_texts(text, project_id, session_id, language_code):
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    return response.query_result.fulfillment_text


def main():
    load_dotenv()
    project_id = os.getenv("PROGECT_ID")
    language_code = os.getenv("LANGUAGE_CODE")
    session_id = os.getenv("SESSION_ID")
    text = ""
    detect_intent_texts(text, project_id, session_id, language_code)


if __name__ == "__main__":
    main()
