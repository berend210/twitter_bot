import db
import filter
import openai3
import twitter
import setup


# Check functions
def update():
    # TODO: fix that we don't only get mentions but replies as well
    last_id = db.get_last_id()
    twitter.update_mentions(last_id=last_id)
    twitter.update_replies(last_id=last_id)
    twitter.update_timelines(users=setup.get_target_users(), last_id=last_id)


# Post functions
def reply():
    # TODO: use an translator for the replies (EN -> NL)
    tweet = db.get_tweet_for_response()

    if tweet is not None:
        tweet_id = tweet[0]
        tweet_text = tweet[1]

        # Generate a response
        text = filter.filter_all(tweet_text)
        response = openai3.response(prompt=text)

        if response is None:
            return

        # Insert generated response in table
        db.insert_response(response, "openai3")

        # Respond to the tweet & update the Tweets table
        twitter.reply_to_with(tweet_id, response)
        db.update_response(1, tweet_id)

    else:
        pass


def post():  # TODO: generate random tweets
    print("Random generated tweet")
