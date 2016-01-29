import os
import sys
import config
import weekday
import q
import word
import logging

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

mode = sys.argv[1]

if mode == 'weekday':
    weekday.post(conf, dir)
elif mode == 'queue':
    q.post(conf, dir)
elif mode == 'word':
    word.post(conf, dir)


