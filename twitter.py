import db
import setup

api = setup.get_client()


def get_username(id):
    return api.get_user(id=id)[0]['username']


def update_timelines(users, do_print=False):
    """
    COUNTS TOWARDS MONTHLY CAP!!
    Gets a timeline update (latest 10 tweets) from all the targeted users
    optional: print all the results
    :param users: a list of user id's
    """
    targets = get_user_ids(users)
    responses = []

    for target in targets:
        since = db.get_last_id(target)
        db.store(api.get_users_tweets(target, since_id=since), get_username(target), target)

    if do_print:
        for response in responses:
            print(response)

    return responses


def update_mentions(do_print=False):
    id = 1515353783567634446
    response = api.get_users_mentions(id=id, since_id=db.get_last_id(), max_results=10)
    db.store(response=response)

    if do_print is True and response[0] is not None:
        print(response)
        for tweet in response[0]:
            print(tweet)

    return response


def build_tweet(input, is_retarded=False):
    text = input
    if is_retarded:
        text = ret_speech(text)
    response = post_tweet(text)
    print(response)


def reply_to_with(tweet_id, text):
    """
    Replies to comment tweet_id with reply reply
    :param tweet_id: comment to reply on
    :param text: the reply that will be posted
    """
    api.create_tweet(text=text, in_reply_to_tweet_id=tweet_id)


def post_tweet(tweet):
    """
    Posts tweet to the Twitter API
    :param tweet: Tweet to be posted to the API
    :return: status of creation of the tweet
    """
    return api.create_tweet(text=tweet)


def get_user_ids(list):
    """
    Sets all the ids for the users,
    so we only have to input usernames
    """
    target_ids = []
    for target in list:
        user = api.get_user(username=target)
        target_ids.append(user.data.id)

    return target_ids


def ret_speech(original_text):
    """
    Converts a string literal to a version where capital letters
    are interchanged with normal letters in alternating fashion.
    :param: original_text: string of input words to be converted
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

