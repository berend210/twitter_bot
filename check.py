import db


# Store in db function
def store(response, username, user_id):
    """
    Function that process the tweet response to store it in a db
    :param response: Response object gotten with a GET request
    :param username: Username from the tweets owner
    :param user_id: User id from the tweets owner
    """
    data = response[0]
    for tweet in data:
        if db.check_tweet_id(tweet["id"]) == 0:
            db.add_tweet(tweet["text"], tweet["id"], user_id, username, False)


# Check functions
