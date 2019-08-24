import requests
import os
from dotenv import load_dotenv
load_dotenv()

def luis_api(text):

    querystring = {"verbose":"false","timezoneOffset":"-360","subscription-key":os.getenv("LUIS_KEY"),"q":text}

    headers = {
        'cache-control': "no-cache",
        }

    response = requests.request("GET", os.getenv("LUIS_ENDPOINT"), headers=headers, params=querystring)
    return response.text