This is a tiny fun project connecting ChatGPT and Slack APIs to send
daily messages in the style of the famous Coelho quotes, but about
programming.

To run the Python script, you need to provide two env vars:

- `OPENAI_KEY`: your OpenAI key
- `SLACK_WEBHOOK`: a Slack Webhook URL tied to a channel

Then run the script:

```sh
python quote.py
```

If you want to set this up to automatically post messages in your Slack 
channel, just fork the repo, set up the above env vars as secrets in 
GitHub Actions, and you are ready to go!

Optionally fine-tune the time of the scheduler in `.github/workflows/daily-post.yml` 
(defined by UTC), and feel free to edit the prompt in the `quote.py` as well.

Contributions welcomed!
## License

Licensed under MPL-2.0, contributions welcomed!
