import os
import sys
import config
import weekday
import q
import word
import logging
import quote

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# is right number of arguments
if len(sys.argv) != 3:
    logging.error('Please enter a mode and file path.')
    sys.exit(1)

dir = sys.argv[2]

# is legal file path
if not os.path.exists(dir):
    logging.error('Please enter a valid file path.')
    sys.exit(1)

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
    conf.error('Invalid mode. Try "weekday", "queue", "word" or "quote"')
