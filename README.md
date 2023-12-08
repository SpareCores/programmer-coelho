# The Programmer Coelho

This is a tiny fun project connecting ChatGPT and Slack APIs to send
daily messages in the style of the famous Coelho quotes, but about
programming.

## Setting up

This is a super basic Python script with minimal dependencies, 
but you need to provide two environment variables:

- `OPENAI_KEY`: your OpenAI key
- `SLACK_WEBHOOK`: a Slack Webhook URL tied to a channel

Then run the script:

```sh
python quote.py
```

## Automation, options

If you want to set this up to automatically post messages in your Slack 
channel, just fork the repo, set up the above env vars as secrets in 
GitHub Actions, and you are ready to go!

Optionally fine-tune the time of the scheduler in `.github/workflows/daily-post.yml` 
(defined by UTC), and feel free to edit the prompt in the `quote.py` as well.

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
