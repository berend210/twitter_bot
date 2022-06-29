import sqlite3

conn = sqlite3.connect('bot.db')
c = conn.cursor()

"""
Create tables if they aren't present
"""
# Creates table 'Tweets'
c.execute("CREATE TABLE IF NOT EXISTS Tweets ("
          "id INTEGER PRIMARY KEY AUTOINCREMENT, "
          "tweet_text VARCHAR(255) NOT NULL, "
          "tweet_id INT NOT NULL, "
          "acc_id INT, "
          "acc_name VARCHAR(255), "
          "response BOOLEAN)")

# Creates table 'Response'
c.execute("CREATE TABLE IF NOT EXISTS Response ("
          "id INTEGER PRIMARY KEY AUTOINCREMENT, "
          "text VARCHAR(255) NOT NULL, "
          "type VARCHAR(255) NOT NULL )")

conn.commit()

"""
Queries for Tweets
"""


def add_tweet(tweet_text, tweet_id, acc_id, acc_name, response):
    """
    Function to add a tweet to the Tweets db
    :param tweet_text: The text in a tweet
    :param tweet_id: The id from a tweet
    :param acc_id: The id from the account that posted the tweet
    :param acc_name: The Twitter name from the account
    :param response: A bool that's used to check if the bot has responded to the tweet
    """
    c.execute("INSERT INTO Tweets (tweet_text, tweet_id, acc_id, acc_name, response)"
              "VALUES (?, ?, ?, ?, ?)", (tweet_text, tweet_id, acc_id, acc_name, response))
    conn.commit()


def check_tweet_id(tweet_id):
    c.execute("SELECT COUNT(*) FROM Tweets WHERE tweet_id = ?", (tweet_id,))
    count = c.fetchall()[0][0]
    conn.commit()
    return count


def get_last_id(acc_name=None):
    if acc_name:
        c.execute("SELECT tweet_id FROM Tweets WHERE acc_name = ? ORDER BY tweet_id desc LIMIT 1", (acc_name,))
    else:
        c.execute("SELECT tweet_id FROM Tweets ORDER BY tweet_id desc LIMIT 1")

    try:
        tweet_id = c.fetchall()[0][0]
        conn.commit()
    except:
        tweet_id = 1538571609807769601

    return tweet_id

def get_tweet_for_response():
    try:
        c.execute("SELECT tweet_id, tweet_text, acc_name FROM Tweets WHERE response = 0 ORDER BY tweet_id LIMIT 1")
        tweet = c.fetchall()[0]
        conn.commit()
    except:
        return None

    return tweet


def update_response(bool, tweet_id):
    c.execute("UPDATE Tweets SET response = ? WHERE tweet_id = ?", (bool, tweet_id))


def insert_response(text, type):
    c.execute("INSERT INTO Response (text, type) VALUES (?, ?)", (text, type))


"""
Functions
"""


# Store in db function
def store(response, username=None, user_id=None):
    """
    Function that process the tweet response to store it in a db
    :param response: Response object gotten with a GET request
    :param username: Username from the tweets owner if provided
    :param user_id: User id from the tweets owner if provided
    """
    if response[0] is None:
        return None

    data = response[0]
    for tweet in data:
        if check_tweet_id(tweet["id"]) == 0:
            add_tweet(tweet["text"], tweet["id"], user_id, username, False)
