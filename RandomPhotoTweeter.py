import os
import sys
import random
import logging
import tweepy
import datetime
import json

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
fileType = 'jpeg', 'jpg', 'png', 'webp', 'gif'
maxSize = 3

today = datetime.datetime.now().strftime("%A")

if len(sys.argv) > 1:
    dir = str(sys.argv[1])
    while not os.path.exists(dir):
        dir = input('Not a valid file path, please try again: ')
else:
    dir = input("Enter your picture folder path: ")
    while not os.path.exists(dir):
        dir = input('Not a valid file path, please try again: ')

try:
    config = open(os.path.join(dir, 'config.json'), 'r')
    logging.debug('Opening: ' + os.path.join(dir, 'config.json'))

    try:
        settings = json.load(config)
    except:
        input('Config file corrupted.')
        config.close()
        sys.exit(1)

    picLast = settings['picOld']
    config.close()
except IOError:
    fileMade = False
    print('No config file in that location, creating one now..')
    while not fileMade:
        try:
            config = open(os.path.join(dir, 'config.json'), 'w')

            key = {'consumerKey': input('Enter your Consumer key: '),
                   'consumerSecret': input('Enter your Consumer Secret: '),
                   'accessToken': input('Enter your Access Token: '),
                   'accessTokenSecret': input('Enter your Access Token Secret: ')
                   }

            monday = ['I love Mondays', 'I cant believe its already Monday', 'It\'s Monday']
            tuesday = ['I love Tuesdays', 'I cant believe its already Tuesday', 'It\'sTuesday']
            wednesday = ['I love Wednesdays', 'I cant believe its already Wednesday', 'It\'s Wednesday']
            thursday = ['I love Thursdays', 'I cant believe its already Thursday', 'It\'s Thursday']
            friday = ['I love Fridays', 'I cant believe its already Friday', 'It\'s Friday']
            saturday = ['I love Saturdays', 'I cant believe its already Saturday', 'It\'s Saturday']
            sunday = ['I love Sundays', 'I cant believe its already Sunday', 'It\'s Sunday']

            update = {'Monday': monday,
                      'Tuesday': tuesday,
                      'Wednesday': wednesday,
                      'Thursday': thursday,
                      'Friday': friday,
                      'Saturday': saturday,
                      'Sunday': sunday}
            picOld = ''

            settings = {'key': key,
                        'update': update,
                        'picOld': picOld}
            json.dump(settings, config, indent=4)
            logging.debug('Creating: ' + os.path.join(dir, 'config.json'))
            config.close()
            picLast = ''

            fileMade = True

            print('Config file created in : ' + dir)
            print('Exit now and open the config.json file if you wish to customize your statuses.')
            input('Otherwise continue with the defaults.')

        except:
            dir = input('Not a valid file path, please try again: ')

auth = tweepy.OAuthHandler(settings['key']['consumerKey'], settings['key']['consumerSecret'])
auth.secure = True
auth.set_access_token(settings['key']['accessToken'], settings['key']['accessTokenSecret'])

tweet = tweepy.API(auth)

pic = os.path.join(dir, random.choice(os.listdir(dir)))

try:
    while (pic == picLast) or (os.path.getsize(pic) > (maxSize * 1000000)) or (not pic.endswith(fileType)):
        if pic == picLast:
            logging.debug('Same pic: ' + pic)
        elif not pic.endswith(fileType):
            logging.debug('Not a pic: ' + pic)
        elif os.path.getsize(pic) > (maxSize * 1000000):
            logging.debug('Pic too big: ' + pic)

        pic = os.path.join(dir, random.choice(os.listdir(dir)))
except:
    input('Error reading files.')
    sys.exit(1)

logging.debug('Posting: ' + pic)
status = random.choice(settings['update'][today])

try:
    logging.disable(logging.INFO)
    tweet.update_with_media(pic, status=status)
    logging.disable(logging.NOTSET)
except:
    print('Authentication failed, please check your keys in the congif file.')
    os.system("Pause")
    sys.exit(1)


settings['picOld'] = pic

config = open(os.path.join(dir, 'config.json'), 'w')
json.dump(settings, config, indent=3)
config.close()
logging.debug('Done, successfully posted: ' + pic + ', with the status: ' + status)
