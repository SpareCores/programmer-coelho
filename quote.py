# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import requests
import os


def askai(prompt):
    """Ask ChatGPT and return a response."""
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
    return response.json().get('choices')[0].get('message').get('content')


prompt = '''
Generate an imperative short sentence that sounds like written by Paulo Coelho, but for programmers. It needs to have programming context, and must be very inspiring, motivational, and funny. Keep it short: one sentence, maximum 160 characters! Pick one or a few from the below list and argue about the importance:
- clean code
- perfect software
- importance of unit testing
- dead code
- good documentation
- joy of the users
- intuitive user interface
- great user experience
- don't build technical debt
- fix bugs
- always improve UX
- linting code
- test coverage
- clean commit history
- descriptive git commit messages
- coding standard
- readable code
- security
- refactor
- ship fast
- efficiency
- simplicity
- open-source
'''

quote = askai(prompt)

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
    if len(quote) > 160:
        quote = askai('Shorten this text to be less than 158 characters:' + quote)
    client.create_tweet(text=quote)

# local post
print(quote)
