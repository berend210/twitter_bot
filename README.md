# Twitter Bot
We're gonna build a twitter bot that's able to respond to other users with generated messages.

# Dependencies
To use this bot you will need to install the following packages:
- Tweepy
- OpenAI GPT-3
- Scheduler

# Setup
The `setup.py` file should be used to manage all your tokens. 
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
```