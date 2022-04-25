import sqlite3

conn = sqlite3.connect('bot.db')
c = conn.cursor()

"""
Create tables if they aren't present
"""
# Creates table 'Tweets'
c.execute("CREATE TABLE IF NOT EXISTS Tweets ("
          "id INTEGER PRIMARY KEY AUTOINCREMENT, "
          "tweet_text VARCHAR(255), "
          "tweet_id INT NOT NULL, "
          "acc_id INT NOT NULL, "
          "acc_name VARCHAR(255), "
          "response BOOLEAN)")

#Creates table 'Response'
c.execute("CREATE TABLE IF NOT EXISTS Response ("
          "id INTEGER PRIMARY KEY AUTOINCREMENT, "
          "text VARCHAR(255) NOT NULL, "
          "type VARCHAR(255) NOT NULL )")

conn.commit()


"""
Queries for Tweets
"""


def add_tweet(tweet_text, tweet_id, acc_id, acc_name, response):
    # Function to insert a tuple in the tweets
    c.execute("INSERT INTO Tweets (tweet_text, tweet_id, acc_id, acc_name, response)"
              "VALUES (?, ?, ?, ?, ?)", (tweet_text, tweet_id, acc_id, acc_name, response))
    conn.commit()


add_tweet("bla", 123, 456, "dick", True)

