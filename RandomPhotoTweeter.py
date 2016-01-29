import os
import sys
import logging
import tweepy
import config
import weekday

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# is there a file path given
if len(sys.argv) > 1:
    dir = str(sys.argv[1])
    while not os.path.exists(dir):
        dir = input('Not a valid file path, please try again: ')
else:
    dir = input("Enter your picture folder path: ")
    while not os.path.exists(dir):
        dir = input('Not a valid file path, please try again: ')

settings = config.Config(dir)

auth = tweepy.OAuthHandler(settings.consumer_key(), settings.consumer_secret())
auth.secure = True
auth.set_access_token(settings.access_token(), settings.access_token_secret())

tweet = tweepy.API(auth)

post = weekday.post(settings, dir)

pic = post[0]
status = post[1]
try:
    logging.disable(logging.INFO)
    tweet.update_with_media(pic, status=status)
    logging.disable(logging.NOTSET)
except:
    print('Authentication failed, please check your keys in the congif file.')
    os.system("Pause")
    sys.exit(1)

settings.set_old_pic(pic)
settings.save()

logging.debug('Done, successfully posted: ' + pic + ', with the status: ' + status)
