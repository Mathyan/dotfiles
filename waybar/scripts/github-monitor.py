#!/usr/bin/env python
import json
import requests
import time
import os

try:
    # Send a request to github.com
    response = requests.get('https://github.com', timeout=5)

    # If the response status code is 200, github.com is reachable
    if response.status_code == 200:
        data = {"text": "✅ Github Status", "class": "check"}
    else:
        data = {"text": "❗ Github Status", "class": "exclamation"}
        os.system('notify-send "Github monitor" "Github.com is unreachable"')

except (requests.ConnectionError, requests.Timeout):
    data = {"text": "❗ Github Status", "class": "exclamation"}
    os.system('notify-send "Github monitor" "Github.com is unreachable"')

print(json.dumps(data))
