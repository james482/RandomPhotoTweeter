import tweet


def post(conf, dir):
    try:
        status = conf.get_queue().pop()
    except IndexError:
        status = 'What a day!'

    tweet.tweet(conf, status)
    return
