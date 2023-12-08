This is a tiny fun project connecting ChatGPT and Slack APIs to send
daily messages in the style of the famous Coelho quotes, but about
programming.

To run the Python script, you need to provide two env vars:

- `OPENAI_KEY`: your OpenAI key
- `SLACK_WEBHOOK`: a Slack Webhook URL tied to a channel

```sh
python quote.py
```
