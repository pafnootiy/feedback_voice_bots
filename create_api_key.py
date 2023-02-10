from google.cloud import api_keys_v2
from google.cloud.api_keys_v2 import Key
import os

from dotenv import load_dotenv

load_dotenv()

project_id = os.getenv("PROGECT_ID")

def create_api_key(project_id )  :
    """
    Creates and restrict an API key.

    TODO(Developer):
    1. Before running this sample,
      set up ADC as described in https://cloud.google.com/docs/authentication/external/set-up-adc
    2. Make sure you have the necessary permission to create API keys.
    3. Make sure  you enable API SERVICE !!!!!!
         "https://console.developers.google.com/apis/api/apikeys.googleapis.com/ "

    Args:
        project_id: Google Cloud project id.

    Returns:
        response: Returns the created API Key.

    

    """

    # Create the API Keys client.
    client = api_keys_v2.ApiKeysClient()

    key = api_keys_v2.Key()
    key.display_name = "My first API key"

    # Initialize request and set arguments.
    request = api_keys_v2.CreateKeyRequest()
    request.parent = f"projects/{project_id}/locations/global"
    request.key = key

    # Make the request and wait for the operation to complete.
    response = client.create_key(request=request).result()

    print(f"Successfully created an API key: {response.name}")
    print(f"key_string: {response.key_string}")
    print(f"response.name: {response.name}")
    # For authenticating with the API key, use the value in "response.key_string".
    # To restrict the usage of this API key, use the value in "response.name".
    return response

create_api_key(project_id ) 