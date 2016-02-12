import tweet


def post(conf):
    try:
        status = conf.get_queue().pop()
    except IndexError:
        conf.error('The Queue is empty.')

    tweet.tweet(conf, status)
    return
