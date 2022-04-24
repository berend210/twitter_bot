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

# from tinydb import TinyDB, Query, where
#
# """
# Variables
# """
# db = TinyDB('db.json')                  # initializes the Database
# account_table = db.table('accounts')    # Initializes the account table
# tweets_table = db.table('tweets')       # Initializes the tweets table
# query = Query()
#
# """
# Classes and Functions
# """
#
#
# class Account:  # class to store Twitter accounts
#     def __init__(self, name, twitter_id):
#         self.name = name
#         self.twitter_id = twitter_id
#
#
# def get_account_id(Account):
#     return account_table.search(query.twitter_id == Account.twitter_id)
#
#
# def add_account(Account):        # Adds an account to the database
#     if Account.twitter_id not in account_table.search(query.id == Account.twitter_id):
#         account_table.insert({'name': Account.name, 'twitter_id': Account.twitter_id})
#
#
# def remove_account(Account):
#     if Account.twitter_id in account_table.search(query.twitter_id == Account.twitter_id):
#         account_table.remove(where('twitter_id') == Account.twitter_id)
#
#
#
#
# def test_account_table():
#     x = Account("Beer", 1234)
#     y = Account("Matt", 5678)
#     remove_account(x)
#     print(get_account_id(x))
#
#
# test_account_table()
# print(account_table.all())