import filter
import setup

""""
Variables
"""
client = setup.get_client()
#               dommee bitch  HEEEEL INTERESSANT
target_list = ['thierrybaudet', 'langefrans']
target_ids_list = [367703310, 45412015]



"""
Functions
"""
# Method for testing methods and api calls
def testing():

	# Posts a retard speech tweet with message of input string
	#twitter.build_tweet("HelloWorlD!", True)

	# Gets the information from a user, to extract ID
	# get_user_response("langefrans")

	# response = client.get_users_tweets(1515353783567634446)
	# print(response.data[0].text)
	#
	# for character in response.data[0].text:
	# 	print(str(character), ", ", ord(character))
	#target_ids_list = get_user_ids()

	text = "Met Gijs en @berryoost ; voor alle mensen aan de hossel. https://t.co/xiKniUeVJP https://t.co/6VKJPMRhVf"
	result = filter.filter_url(text)
	print(result)
	pass



def get_user_ids():
	"""
	Sets all the ids for the users,
	so we only have to input usernames
	"""
	target_ids = []
	for target in target_list:
		user = client.get_user(username=target)
		target_ids.append(user.data.id)

	# for id in target_ids:
	# 	print(id)

	return target_ids

def get_user_response(username):
	user = client.get_user(username=username)
	print("USER: " + str(user))
	return user

""""
Executables
"""
if __name__ == "__main__":
	testing()

