import db
import filter
import openai3
import twitter
import setup
import random
import logger


# Check functions
def update():
    """
    Job which updates all the tweets the bot checks on.
    :return: None
    """
    last_id = db.get_last_id()
    twitter.update_mentions(last_id=last_id)
    twitter.update_replies(last_id=last_id)
    twitter.update_timelines(users=setup.get_target_users(), last_id=last_id)
    logger.log("Updated Tweets in check.py.")


# Post functions
def reply():
    """
    Replies to all the non-replied Tweets in the database.
    :return: None
    """
    tweet = db.get_tweet_for_response()

    if tweet is not None:
        tweet_id = tweet[0]
        tweet_text = tweet[1]
        tweet_acc = tweet[2]

        # Has a chance of replying on someone's tweet
        if tweet_acc is not None and random.randint(0, 10) > 7:
            db.update_response(1, tweet_id)
            logger.log("Not responded to: " + tweet_id + ", has been processed.")
            return

        # Generate a response
        text = filter.filter_all(tweet_text)
        response = openai3.response(prompt=text)

        if response is None:
            return

        # Respond to the tweet & update the Tweets table
        success = twitter.reply_to_with(tweet_id, response)

        if not success:
            return

        # Insert generated response in table
        db.insert_response(response, "openai3")
        db.update_response(1, tweet_id)
        logger.log("Responded to: " + str(tweet_id) + ". Text: " + response)


def post():  # TODO: generate random tweets
    # Let the openai resond to messages we created
    # Fetch the openai random tweets from Twitter and use that to make posts
    # Send random words to openai to invoke some reaction
    print("Random generated tweet")
