import os
import logging
import random
import datetime
import tweet


def get_size(pic, max_size):
    try:
        if os.path.getsize(pic) > (max_size * 1000000):
            return True
        else:
            return False
    except PermissionError:
        return True


def post(conf, dir):
    file_type = conf.get_file_types()
    max_size = conf.get_max_size()
    pic_last = conf.get_old_pic()
    today = datetime.datetime.now().strftime("%A")

    # load files into a list
    files = os.listdir(dir)
    # shuffle the list
    random.shuffle(files)

    # try popping until one is found
    try:
        pic = os.path.join(dir, files.pop())
        while (pic == pic_last) or get_size(pic, max_size) or (not pic.endswith(file_type)):
            pic = os.path.join(dir, files.pop())
    # exit if non are found
    except IndexError:
        conf.error('No suitable picture found.')

    try:
        status = random.choice(conf.get_status_day(today))
    except IndexError:
        conf.error('No statuses set for ' + today + '.')

    logging.debug('Posting: ' + pic)
    p = [pic, status]
    tweet.tweet_with_pic(conf, p)
    return
