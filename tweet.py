import tweepy
import logging


def tweet(conf, post):
    auth = tweepy.OAuthHandler(conf.get_consumer_key(), conf.get_consumer_secret())
    auth.secure = True
    auth.set_access_token(conf.get_access_token(), conf.get_access_token_secret())

    t = tweepy.API(auth)
    try:
        logging.disable(logging.INFO)
        t.update_status(post)
        logging.disable(logging.NOTSET)
    except:
        conf.error('Authentication failed, please check your keys in the config file,'
                   'Or could be a duplicate tweet.')

    conf.save()

    logging.debug('Done, successfully posted the status: ' + post)
    return


def tweet_with_pic(conf, post):
    auth = tweepy.OAuthHandler(conf.get_consumer_key(), conf.get_consumer_secret())
    auth.secure = True
    auth.set_access_token(conf.get_access_token(), conf.get_access_token_secret())

    t = tweepy.API(auth)
    pic = post[0]
    status = post[1]
    try:
        logging.disable(logging.INFO)
        t.update_with_media(pic, status=status)
        logging.disable(logging.NOTSET)
    except:
        conf.error('Authentication failed, please check your keys in the congif file.')

    conf.set_old_pic(pic)
    conf.save()

    logging.debug('Done, successfully posted: ' + pic + ', with the status: ' + status)
    return
