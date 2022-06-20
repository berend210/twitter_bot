import check
import filter
import setup
import schedule
import time


""""
Variables
"""
client = setup.get_client()

target_list = setup.get_target_users()
target_ids_list = [367703310, 45412015]

"""
Functions
"""


# Method for testing methods and api calls
def testing():
    text = "Met Gijs en @berryoost ; voor alle mensen aan de hossel. https://t.co/xiKniUeVJP https://t.co/6VKJPMRhVf"
    result = filter.filter_all(text)
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

    return target_ids


def get_user_response(username):
    user = client.get_user(username=username)
    print("USER: " + str(user))
    return user


""""
Executables
"""


# if __name__ == "__main__":
#     testing()


"""
Scheduler
"""
# Updating the timelines
# Importing random tweets
# Replying to other people
# Posting random tweets


# Updates the mentions every 5 minutes
schedule.every(2).minutes.do(check.update)
# Updates the tweets db every 5 minutes
schedule.every(2).minutes.do(check.reply)

# TODO: Uncomment the code underneath when work on the scheduler is done
while True:
    schedule.run_pending()
    time.sleep(1)
