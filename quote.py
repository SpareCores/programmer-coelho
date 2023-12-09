# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import requests
import os

prompt = '''
Generate an imperative short sentence that sounds like written by Paulo Coelho, but for programmers. It needs to have programming context, and must be very inspiring, motivational, and funny. Keep it short: one sentence, maximum 160 characters! Pick one or a few from the below list and argue about the importance:
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

# slack post
if os.getenv('SLACK_WEBHOOK'):
    requests.post(
        os.getenv('SLACK_WEBHOOK'),
        headers={'Content-type': 'application/json'},
        json={'text': quote})

# twitter post
if os.getenv('TWITTER_CLIENT_ID') and \
   os.getenv('TWITTER_CLIENT_SECRET') and \
   os.getenv('TWITTER_ACCESS_TOKEN') and \
   os.getenv('TWITTER_ACCESS_TOKEN_SECRET'):
    import tweepy
    client = tweepy.Client(
        consumer_key=os.environ['TWITTER_CLIENT_ID'],
        consumer_secret=os.environ['TWITTER_CLIENT_SECRET'],
        access_token=os.environ['TWITTER_ACCESS_TOKEN'],
        access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET']
    )
    client.create_tweet(text=quote)

# local post
print(quote)
