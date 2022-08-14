import tweepy.errors
from datetime import datetime, timedelta
import db
import setup
import logger

api = setup.get_client()


def get_username(id):
    """
    Functions which returns the id's username.
    :param id: integer from user id.
    :return: username string.
    """
    return api.get_user(id=id)[0]['username']


def update_timelines(users, last_id, do_print=False):
    """
    Gets the last timeline updates from target users.
    :param users: username list.
    :param last_id: integer of last fetched Tweet id.
    :param do_print: boolean for printing the results.
    :return: Response object.
    """
    targets = get_user_ids(users)
    responses = []
    since_date = None

    if last_id == None:
        since_date = datetime.now() - timedelta(days=6)

    for target in targets:
        db.store(api.get_users_tweets(target, since_id=last_id, max_results=5, start_time=since_date), get_username(target), target)

    if do_print:
        for response in responses:
            print(response)

    return responses


def update_mentions(last_id, do_print=False):
    """
    Gets the last 10 @mentions from Twitter if they haven't been fetched already.
    :param last_id: integer of last fetched Tweet id.
    :param do_print: boolean for printing the results.
    :return: Response object.
    """
    id = 1515353783567634446
    
    since_date = None

    if last_id == None:
        since_date = datetime.now() - timedelta(days=6)
    
    response = api.get_users_mentions(id=id, since_id=last_id, max_results=10, start_time=since_date)
    db.store(response=response)

    if do_print is True and response[0] is not None:
        print(response)
        for tweet in response[0]:
            print(tweet)

    return response


def update_replies(last_id, do_print=False):
    """
    Gets the last replies to the bot's Tweets.
    :param last_id: integer of last fetched Tweet id.
    :param do_print: boolean for printing the results.
    :return: Response object.
    """
    
    since_date = None

    if last_id == None:
        since_date = datetime.now() - timedelta(days=6)
    
    response = api.search_recent_tweets(query="to:" + setup.get_bot_name(), since_id=last_id, max_results=10, start_time=since_date)
    db.store(response=response)

    if do_print is True and response[0] is not None:
        print(response)
        for tweet in response[0]:
            print(tweet)

    return response


def reply_to_with(tweet_id, text):
    """
    Replies to comment tweet_id with reply.
    :param tweet_id: comment to reply on.
    :param text: the reply that will be posted.
    """
    try:
        api.create_tweet(text=text, in_reply_to_tweet_id=tweet_id)
    except Exception as inst:
        print("ERROR: ")
        print(type(inst))
        logger.log("ERROR: " + repr(inst) + ", " + str(inst))
        if type(inst) == tweepy.errors.Forbidden:
            return True

        return False
    return True


def post_tweet(tweet, is_ret=False):
    """
    Posts tweet to the Twitter API
    :param is_ret: Boolean for making a ret Tweet
    :param tweet: Tweet to be posted to the API
    :return: status of creation of the tweet
    """
    if is_ret:
        tweet = ret_speech(tweet)
    return api.create_tweet(text=tweet)


def get_user_ids(list):
    """
    Gets all user ids from a username list
    :param list: list with usernames
    :return: a list with usernames
    """
    target_ids = []
    for target in list:
        user = api.get_user(username=target)
        target_ids.append(user.data.id)

    return target_ids


def ret_speech(original_text):
    """
    Converts a string literal to a version where capital letters
    are interchanged with normal letters in alternating fashion
    :param: original_text: string of inp words to be converted
    :return: original text, but in ret speech, aka "Hello World!" -> "hElLo WoRlD!"
    """
    original_text = original_text.casefold()
    result_list = []
    for i, element in enumerate(original_text):
        if i % 2 != 0:
            result_list.append(element.upper())
        else:
            result_list.append(element)

    result_text = ""
    for c in result_list:
        result_text += c

    return result_text
