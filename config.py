import os
import sys
import logging
import tweepy
import config
import weekday
import q

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# is there a file path given
if len(sys.argv) > 2:
    dir = str(sys.argv[2])
    print(sys.argv[2])
    while not os.path.exists(dir):
        dir = input('Not a valid file path, please try again: ')
else:
    dir = input("Enter your picture folder path: ")
    while not os.path.exists(dir):
        dir = input('Not a valid file path, please try again: ')

settings = config.Config(dir)

mode = sys.argv[1]

if mode == 'weekday':
    post = weekday.post(settings, dir)
elif mode == 'queue':
    post = q.post(settings, dir)

auth = tweepy.OAuthHandler(settings.get_consumer_key(), settings.get_consumer_secret())
auth.secure = True
auth.set_access_token(settings.get_access_token(), settings.get_access_token_secret())

tweet = tweepy.API(auth)


pic = post[0]
status = post[1]
try:
    logging.disable(logging.INFO)
    #tweet.update_with_media(pic, status=status)
    os.startfile(pic)
    logging.disable(logging.NOTSET)
except:
    print('Authentication failed, please check your keys in the congif file.')
    os.system("Pause")
    sys.exit(1)

settings.set_old_pic(pic)
settings.save()

logging.debug('Done, successfully posted: ' + pic + ', with the status: ' + status)
