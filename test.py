import requests
import json


res = requests.post('http://192.168.1.115:8000',
                data={"ticker": "AMD"}
                ).json()

print(res)