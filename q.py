import weekday
import random
import datetime


def post(conf, dir):
    pic = weekday.post(conf, dir)[0]
    today = datetime.datetime.now().strftime("%A")

    try:
        status = conf.get_queue().pop()
    except IndexError:
        status = random.choice(conf.get_status_day(today))

    p = [pic, status]
    return p
