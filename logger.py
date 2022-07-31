import logging

logging.basicConfig(filename='bot.log', format='%(asctime)s : %(message)s', level=logging.INFO)
logging.info('----------- logging started -------------')

def log(message):
    logging.info(message)


log("The crontab works! Hooray :)")
print("croonnnieijiefjdalf")