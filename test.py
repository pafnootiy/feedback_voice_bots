# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import dialogflow_v2

def sample_detect_intent():
    # Create a client
    client = dialogflow_v2.SessionsClient()

    # Initialize request argument(s)
    request = dialogflow_v2.DetectIntentRequest(
        session="session_value",
    )

    # Make the request
    response = client.detect_intent(request=request)

    # Handle the response
    print(response)