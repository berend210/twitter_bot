import check
import setup
import schedule
import time


""""
Variables
"""
client = setup.get_client()

"""
Schedulers
"""

# Updates the mentions every 5 minutes
schedule.every(2).minutes.do(check.update)
# Updates the Tweets db every 5 minutes
schedule.every(2).minutes.do(check.reply)
print("Twitter bot ready.")

while True:
    schedule.run_pending()
    time.sleep(1)
