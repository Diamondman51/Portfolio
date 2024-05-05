import requests
import json

def get_currency():
    url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'
    text = json.loads(requests.get(url).text)
    return text[:3]
# print(get_currency())