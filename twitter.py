import main

api = main.client

def update_timelines(start_time = None, do_print = False):
	"""
	COUNTS TOWARDS MONTHLY CAP!!
	Gets a timeline update (latest 10 tweets) from all the targeted users
	optional: print all the results
	"""
	targets = main.target_ids_list
	responses = []

	if (start_time != None):
		pass
		# TODO: api call that inludes start_time (uses Oauth2.0)
		# for target in targets:
		# 	responses.append(api.get_users_tweets(start_time=s start_time target))

	for target in targets:
		responses.append(api.get_users_tweets(target))

	if do_print:
		for response in responses:
			print(response)

	return responses


def build_tweet(input, is_retarded = False):
	text = input
	if is_retarded:
		text = ret_speech(text)
	response = post_tweet(text)
	print(response)

def post_tweet(tweet):
    """
    Posts tweet to the Twitter API
    :param tweet: Tweet to be posted to the API
    :return: status of creation of the tweet
    """
    return api.create_tweet(text=tweet)


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