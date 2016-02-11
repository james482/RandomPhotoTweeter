import tweet
import os
import sys
import logging


def post(conf):
    try:
        status = conf.get_queue().pop()
    except IndexError:
        logging.error('The Queue is empty.')
        os.system("Pause")
        sys.exit(1)

    tweet.tweet(conf, status)
    return
