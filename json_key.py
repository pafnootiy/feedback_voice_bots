import requests
import telegram
import os
from dotenv import load_dotenv
from telegram.ext import Updater, MessageHandler, Filters
from google.cloud import storage
load_dotenv()

tg_token=os.getenv("TG_API_TOKEN")
project_id=os.getenv("PROGECT_ID")
language_code=os.getenv("LANGUAGE_CODE")
session_id=os.getenv("SESSION_ID")
print(tg_token)



def authenticate_implicit_with_adc(project_id=project_id):
    """
    When interacting with Google Cloud Client libraries, the library can auto-detect the
    credentials to use.

    // TODO(Developer):
    //  1. Before running this sample,
    //  set up ADC as described in https://cloud.google.com/docs/authentication/external/set-up-adc
    //  2. Replace the project variable.
    //  3. Make sure that the user account or service account that you are using
    //  has the required permissions. For this sample, you must have "storage.buckets.list".
    Args:
        project_id: The project id of your Google Cloud project.
    """

    # This snippet demonstrates how to list buckets.
    # *NOTE*: Replace the client created below with the client required for your application.
    # Note that the credentials are not specified when constructing the client.
    # Hence, the client library will look for credentials using ADC.
    storage_client = storage.Client(project=project_id)
    buckets = storage_client.list_buckets()
    print("Buckets:")
    for bucket in buckets:
        print(bucket.name)
    print("Listed all storage buckets.")
authenticate_implicit_with_adc(project_id=project_id)