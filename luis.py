import requests
import os
from dotenv import load_dotenv
load_dotenv()

def luis_api(text):

    querystring = {"verbose":"false", "show-all-intents":"true", "timezoneOffset":"-360", "log":"false", "subscription-key":os.getenv("LUIS_KEY"),"query":text}

    headers = {
        'cache-control': "no-cache",
        }

    response = requests.request("GET", os.getenv("LUIS_NEW_ENDPOINT"), headers=headers, params=querystring)
    return response.text