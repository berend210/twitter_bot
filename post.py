import main

def post_tweet(tweet):
    """
    Posts tweet to the Twitter API, variable 'client' from main.py
    :param tweet: Tweet to be posted to the API
    :return: nothing, its a void... That's why you don't do drugs kids!
    """
    main.client.create_tweet(tweet)

def ret_speech(original_text):
    """
    :param original_text: string of input words to be converted
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

