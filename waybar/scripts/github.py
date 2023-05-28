#!/usr/bin/env python
import os
import requests

def get_notification_count(username):
    token_file = os.path.expanduser('~/.config/github/notifications.token')
    with open(token_file, 'r') as file:
        token = file.read().strip()

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {token}',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    response = requests.get(f'https://api.github.com/notifications', headers=headers)
    notifications = response.json()
    count = len(notifications)
    print('{{"text": "{}"}}'.format(count))

if __name__ == '__main__':
    username = 'Mathyan'
    get_notification_count(username)
