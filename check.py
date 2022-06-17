import db
import filter
import openai3
import twitter
import setup


# Check functions
def update():  # TODO: put update timelines and mentions in one function
    twitter.update_mentions()
    twitter.update_timelines(users=setup.get_target_users())


# Post functions
def reply():
    tweet = db.get_tweet_for_response()

    if tweet is not None:
        # Generate a response
        text = filter.filter_all(tweet["text"])
        response = openai3.response(prompt=text)

        # Insert generated response in table
        db.insert_response(response, "openai3")

        # Respond to the tweet & update the Tweets table
        twitter.reply_to_with(tweet["tweet_id"], response)
        db.update_response(1, tweet["tweet_id"])

    else:
        pass


def post(): # TODO: generate random tweets
    print("Random generated tweet")
