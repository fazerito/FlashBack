import os
import json
import requests
import uuid
from config import keys

class Client:
    def __init__(self):
        self.API_URL = 'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=pl'
        self.headers = {
            'Ocp-Apim-Subscription-Key': keys['FLASHBACK_T_API_KEY'],
            'Ocp-Apim-Subscription-Region': keys['FLASHBACK_T_API_REGION'],
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

    def translate(self, phrase):
        request_body = [{
            'text': phrase
        }]
        request = requests.post(self.API_URL, headers=self.headers, json=request_body)
        response = request.json()
        print(json.dumps(response, sort_keys=True, indent=4,
                 ensure_ascii=False, separators=(',', ': ')))
