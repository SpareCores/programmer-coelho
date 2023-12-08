# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import requests
import os

prompt = '''
Generate  an imperative sentence that sounds like written by Paulo Coelho, but for programmers. It needs to have programming context, but very inspiring and motivational. Keep it short: one sentence, max 3 lines, imperative style with reasoning. Pick one or a few from the below list and argue about the importance:
- clean code
- perfect software
- importance of unit testing
- good documentation
- joy of the users
- intuitive user interface
- great user experience
- don't build technical debt
- fix bugs
- always improve UX
'''

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + os.getenv('OPENAI_API_KEY'),
}

json_data = {
    'model': 'gpt-3.5-turbo',
    'messages': [
        {
            'role': 'user',
            'content': prompt,
        },
    ],
    'temperature': 0.7,
}

response = requests.post(
    'https://api.openai.com/v1/chat/completions',
    headers=headers, json=json_data)

quote = response.json().get('choices')[0].get('message').get('content')

requests.post(
    os.getenv('SLACK_WEBHOOK'),
    headers={'Content-type': 'application/json'}, 
    json={'text': quote})
