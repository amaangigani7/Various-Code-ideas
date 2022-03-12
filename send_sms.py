
import requests
import json

url = "https://www.fast2sms.com/dev/bulk"
my_data = {
    'sender_id': 'FSTSMS',
    'message': 'This is a test message',
    'language' : "English",
    'route' : 'p',
    'numbers': "9374499699, 9376499699"
}

headers = {
    'authorization': 'Yl73rN54bkAsZXtMHTg1hUJILQGSDjxvoynpEcKezPaCF6q9dfA7tcTM1S8WhYDypXgiEIPNsbwzKkZu',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cache-Control': 'no-cache',
}

response = requests.request('POST', url, data=my_data, headers=headers)
returned_msg = json.loads(response.text)
print(returned_msg['message'])
