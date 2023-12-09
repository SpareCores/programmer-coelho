# The Programmer Coelho

This is a tiny fun project connecting ChatGPT and Slack/Twitter APIs
to send daily messages in the style of the famous Coelho quotes, but
about programming.

Follow on [Twitter](https://twitter.com/DeveloperCoelho) for daily udpates!

## Setting up

This is a super basic Python script with minimal dependencies,
so you need to install Python 3 and a few packages:

```sh
pip install -r requirements.txt
```

Then provide at least the below environment variable:

- `OPENAI_KEY`: your OpenAI key required

Optionally define the below environment variable as well
to post on a Slack channel:

- `SLACK_WEBHOOK`: a Slack Webhook URL tied to a channel

Optionally define the below environment variables as well
to post on Twitter:

- `TWITTER_CLIENT_ID`: the client id form your Consumer Keys
- `TWITTER_CLIENT_SECRET`: the client secret form your Consumer Keys
- `TWITTER_ACCESS_TOKEN`: the access token from your Authentication Tokens
- `TWITTER_ACCESS_TOKEN_SECRET`: the access token secret from your Authentication Tokens

Then run the script:

```sh
python quote.py
```

## Automation

If you want to set this up to automatically post messages in your
Slack channel or on Twitter, just fork the repo, set up the above
required and optional env vars as secrets in GitHub Actions, and you
are ready to go!

Optionally fine-tune the time (UTC) of the scheduler(s) in the YAML
files of `.github/workflows`, and feel free to edit the prompt in the
`quote.py` as well.

## Examples

- "Let the joy of users be your guiding light; in every line of code, cultivate an experience that transcends functionality, resonating with seamless beauty and user satisfaction."
- "Design interfaces intuitively, as though crafting a dialogue between the user and the machine, where each click is a harmonious note in the symphony of great user experience."
- "In the sacred quest for programming excellence, embrace the importance of unit testing, weaving a shield against imperfections and ensuring the resilience of your digital creation."
- "Sculpt clean code with the precision of a master artisan, for it is the foundation upon which perfect software and the joy of users are gracefully built."
- "Document your code as if preserving ancient wisdom, for clarity in documentation is the roadmap to understanding, enabling others to follow the path to brilliance."
- "Guard against the shadows of technical debt, for in the pursuit of progress, leave behind a legacy free from the burdens that hinder innovation and growth."
- "Fix bugs with the diligence of a healer, for in each resolution, you breathe life back into your creation, ensuring its strength and vitality in the ever-evolving digital landscape."
- "Commit to perpetual improvement, for the evolution of UX is a journey without end, where every iteration brings you closer to the zenith of user satisfaction."
- "Craft each line of code as if writing poetry, where the rhythm of clean code and the melody of a bug-free system compose a digital opus that stands the test of time."
- "In the tapestry of programming, weave perfection, as every detail matters; let the symphony of clean code and user-centric design echo in the digital corridors of innovation."

## License

Licensed under MPL-2.0, contributions welcomed!
