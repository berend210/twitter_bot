# Twitter Bot
We've build a twitter bot that's able to respond to other users with generated messages. Make sure to use this bot responsibly since it would be possible to use it for wrong purposes and bad motivations.

# Dependencies
To use this bot you will need to install the following packages:
- Openai.py
- Tweepy.py
- Scheduler.py
- Discord.py
- Deep-translator.py (Google translate)

# Setup
The `setup.py` file should be used to manage all your tokens and sensitive data. 
It should look like this:
```
import tweepy


def get_client():
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    ACCESS_KEY = ''
    ACCESS_SECRET = ''
    BEARER_TOKEN = ''

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    TWclient = tweepy.Client(BEARER_TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET, wait_on_rate_limit=True)
    return TWclient


def test_client():
    client = get_client()
    # Check if they match
    print('Bearer token:' + client.bearer_token + '\nConsumer key: ' + client.consumer_key + '\nConsumer secret: '
          + client.consumer_secret + '\nAccess token: ' + client.access_token + '\nAccess secret: ' + client.access_token_secret)


def get_openai():
    BEARER_TOKEN = ''
    return BEARER_TOKEN
    

def get_discord_token():
    DISCORD_TOKEN = ''
    return DISCORD_TOKEN


def get_target_users():
    target_list = ['nasa'] # Example
    return target_list


def get_prompts():
    prompt_list = [
        ("Give an unknown fact about: .\n", "Type: Unknown fact"),
        ("Give a known fact about: .\n", "Type: Known fact")
    ] # Example
    return prompt_list


def get_bot_name():
    return ""   # Your bot's name
```

# Translator
We currently use the `deep_translator.py` package for translating the tweets to English and the OpenAI responses back to 
Dutch since the ML model isn't capable enough of handling all language inputs.

# Help
If you need any help or have any questions about the project you can contact us via GitHub. We probably respond
to you in ~7 days. Have fun and make sure to think about the ethics of managing a Twitter/Discord bot who
can generate any message he wants.
