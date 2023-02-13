import os

from dotenv import load_dotenv
from google.cloud import dialogflow


def detect_intent_texts(text, project_id, session_id, language_code):
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print("Session path: {}\n".format(session))

    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    if response.query_result.intent.is_fallback:
        print(response.query_result.intent.is_fallback)
        ask_support = "Я не понимаю о чем ты , зову человеков!"
        text_input = dialogflow.TextInput(text=ask_support,
                                          language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)
        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        return response.query_result.query_text

    else:
        print("=" * 20)
        print("Query text: {}".format(response.query_result.query_text))
        print(
            "Detected intent: {} (confidence: {})\n".format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence,
            )
        )
        print("Fulfillment text: {}\n".format(
            response.query_result.fulfillment_text))
        return response.query_result.fulfillment_text

 
def main():
    load_dotenv()

    project_id = os.getenv("PROGECT_ID")
    language_code = os.getenv("LANGUAGE_CODE")
    session_id = os.getenv("SESSION_ID")
    text = ""

    detect_intent_texts(text, project_id, session_id, language_code)

if __name__ == "__main__" :
    main()
