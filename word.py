from PIL import Image
import os
import tweet


def post(conf, dir):
    width = 1024
    height = 512

    pic = Image.new("RGB", (width, height), "blue")
    pic.save(os.path.join(dir, 'pic.jpg'))
    status = ''
    p = [os.path.join(dir, 'pic.jpg'), status]
    tweet.tweet_with_pic(conf, p)
    os.remove(os.path.join(dir, 'pic.jpg'))
    return
