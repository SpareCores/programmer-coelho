# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import requests
import os
import random


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

topics = [
    'unit testing',
    'clean code',
    'dead code',
    '10x programmer',
    'unicorn',
    'framework',
    'logging',
    'good documentation',
    'tech debt',
    'linting',
    'intergration testing',
    'e2e tests',
    'bugs',
    'clean commit history',
    'test coverage',
    'descriptive git commit messages',
    'coding standard',
    'readable code',
    'security',
    'refactor',
    'ship fast',
    'efficiency',
    'simplicity',
    'open-source',
    'user experience',
]
random.shuffle(topics)
topics_markdown = '\n'.join(['- ' + t for t in topics])

prompt = f'''
You are a super senior architect sharing wisdom for junior programmers in the stlye of Paulo Coelho.
Write one, short sentence, maximum 3 lines, which can be shared in social media to train and entertrain
other developers and programmers. Include one or two hastags in the message.

This quote must be extremely inspiring, motivation, and funny. Again, keep it short: one sentence, maximum 3 lines.

The quote should include an educational message about programming best practices. As an example, pick one of the below items (with equal chance for each in the list) or something similar:

{topics_markdown}

And make sure to exagerate to make the message funny, e.g. argue for the importance of any of the above for_current_screen the better good of the universe, joy of the users, intuitive user interfaces etc.
'''

quote = askai(prompt).strip('\"')

# local post
print(quote)

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
        quote = askai(
            'Shorten this text to be less than 160 characters:'
            + quote).strip('\"')
    client.create_tweet(text=quote)
