import os
import sys
import config
import weekday
import q
import word
import logging
import quote

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# is there a file path given
if len(sys.argv) > 2:
    dir = str(sys.argv[2])
    while not os.path.exists(dir):
        dir = input('Not a valid file path, please try again: ')
else:
    dir = input("Enter your picture folder path: ")
    while not os.path.exists(dir):
        dir = input('Not a valid file path, please try again: ')

conf = config.Config(dir)

# set the mode
mode = sys.argv[1]

if mode == 'weekday':
    weekday.post(conf, dir)
elif mode == 'queue':
    q.post(conf)
elif mode == 'word':
    word.post(conf, dir)
elif mode == 'quote':
    quote.post(conf, dir)
else:
    logging.error('Invalid mode.')
    os.system("Pause")
    sys.exit(1)
